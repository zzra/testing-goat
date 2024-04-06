from django.test import TestCase

from lists.models import Item, List
from lists.forms import (
	DUPLICATE_ITEM_ERROR,
	EMPTY_ITEM_ERROR,
	ExistingListItemForm,
	ItemForm
)

class ItemFormTest(TestCase):
	def test_form_renders_id_text_input(self):
		form = ItemForm()
		self.assertIn('placeholder="Enter a to-do item"', form.as_p())
		self.assertIn('class="form-control form-control-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = ItemForm(data={"text":""})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors["text"], ["You can't have an empty list item"])

	def test_form_save_handles_saving_to_a_list(self):
		mylist = List.objects.create()
		form = ItemForm(data={"text": "do me"})
		new_item = form.save(for_list=mylist)
		self.assertEqual(new_item, Item.objects.get())
		self.assertEqual(new_item.text, "do me")
		self.assertEqual(new_item.list, mylist)

class ExistingListItemFormTest(TestCase):
	def test_form_renders_item_text_input(self):
		mylist = List.objects.create()
		form = ExistingListItemForm(for_list=mylist)
		self.assertIn('placeholder="Enter a to-do item"', form.as_p())

	def test_form_validation_for_blank_items(self):
		mylist = List.objects.create()
		form = ExistingListItemForm(for_list=mylist, data={"text":""})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors["text"], [EMPTY_ITEM_ERROR])

	def test_form_validation_for_duplicate_items(self):
		mylist = List.objects.create()
		Item.objects.create(list=mylist, text="no twins!")
		form = ExistingListItemForm(for_list=mylist, data={"text": "no twins!"})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors["text"], [DUPLICATE_ITEM_ERROR])

	def test_form_save(self):
		mylist = List.objects.create()
		form = ExistingListItemForm(for_list=mylist, data={"text": "hi"})
		new_item = form.save()
		self.assertEqual(new_item, Item.objects.all()[0])


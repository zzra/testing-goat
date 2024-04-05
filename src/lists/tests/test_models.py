from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List

class ListAndItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, "")

    def test_item_is_related_to_list(self):
        mylist  = List.objects.create()
        item = Item()
        item.list = mylist
        item.save()
        self.assertIn(item, mylist.item_set.all())
        
    def test_cannot_save_empty_list_items(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text="")
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()

    def test_duplicate_items_are_invalid(self):
        mylist = List.objects.create()
        Item.objects.create(list=mylist, text="duplicate")
        with self.assertRaises(ValidationError):
            item = Item(list=mylist, text="duplicate")
            item.full_clean()
    
    def test_CAN_save_saame_item_to_different_lists(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        Item.objects.create(list=correct_list, text="dup")
        item = Item(list=other_list, text="dup")
        item.full_clean()

    def test_list_ordering(self):
        mylist = List.objects.create()
        first_item = Item.objects.create(list=mylist, text="item one")
        second_item = Item.objects.create(list=mylist, text="item two")
        third_item = Item.objects.create(list=mylist, text="item three")
        self.assertEqual(
            list(Item.objects.all()),
            [first_item, second_item, third_item]
        )

    def test_default_text(self):
        item = Item(text="some text")
        self.assertEqual(str(item), "some text")

class ListModelTest(TestCase):
    def test_get_absolute_url(self):
        mylist = List.objects.create()
        self.assertEqual(mylist.get_absolute_url(), f"/lists/{mylist.id}/")

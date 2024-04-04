from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidnelty tries to submit an empty list item
        # she hits enter on the empty input box

        # the home page refreshes, there is an error message saying "list items cannot be blank"

        # she tries again with some text for the item, it works

        # perversely she now decides to submit another blank item

        # she receives a similar warning for the blank item

        # she can correct it by adding some text
        self.fail("write me!")
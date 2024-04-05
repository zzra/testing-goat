from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # edith goes to the home page and accidnelty tries to submit an empty list item
        # she hits enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)

        # the home page refreshes, there is an error message saying "list items cannot be blank"
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        # she tries again with some text for the item, it works
        self.get_item_input_box().send_keys("Buy milk")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # perversely she now decides to submit another blank item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # she receives a similar warning for the blank item
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
                "You can't have an empty list item",
            )
        )

        # she can correct it by adding some text
        self.get_item_input_box().send_keys("Make tea")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")
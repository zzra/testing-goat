from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NewVistitorTest(FunctionalTest):
    def test_can_start_a_todo_list(self):
        # Edith heard about a cool new online to-do app
        # she goes to check out its homepage
        self.browser.get(self.live_server_url)

        # she notices the page title and head mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # she types "buy peacock feathers" into a text box
        # edith ties fishing lures for fun
        inputbox.send_keys("Buy peacock feathers")

        # when she hits enter the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # there is still a text box inviting her to add another item
        # she enters "Use peacock feathers to make a fly"
        # edith is methodical
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, now shows both items on her list
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # there is still a textbox inviting her to add another item
        # she enters "User peacock feathers to make a fly" edith is methodical
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")

        # the page updates again, showing both items in the list

        # satisifed, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # she notices that her list has a unique url
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")

        # now a new user, Francis, comes along

        ## we delete the browser cookies
        ## to simulate a new user
        self.browser.delete_all_cookies()

        # francis visits the home page, there is no sign of edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        # francis starts a new list by entering a new item, he's boring
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # francis gets his own unique url
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # again, there is no trace of edith's list
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)

        # satisified, they both go back to sleep
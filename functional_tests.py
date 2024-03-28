from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
import unittest
path = "/snap/bin/geckodriver"

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=Service(executable_path=path))

    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_todo_list(self):
        # Edith heard about a cool new online to-do app
        # she goes to check out its homepage
        self.browser.get("http://127.0.0.1:8000")


        # she notices the page title and head mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # she types "buy peacock feathers" into a text box
        # edith ties fishing lures for fun
        inputbox.send_keys("Buy peacock feathers")

        # when she hits enter the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # there is still a text box inviting her to add another item
        # she enters "Use peacock feathers to make a fly"
        # edith is methodical
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page updates again, now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.check_for_row_in_list_table("1: Buy peacock feathers")
        self.check_for_row_in_list_table("2: Use peacocks feathers to make a fly")

        # there is still a textbox inviting her to add another item
        # she enters "User peacock feathers to make a fly" edith is methodical
        self.fail("Finish the test!")

        # the page updates again, showing both items in the list

        # satisifed, she goes back to sleep

if __name__ == "__main__":
    unittest.main()
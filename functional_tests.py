import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
path = "/snap/bin/geckodriver"

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=Service(executable_path=path))

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        self.browser.get("http://127.0.0.1:8000")
        # Edith heard about a cool new online to-do app
        # she goes ot check out its homepage

        self.assertIn("To-Do", self.browser.title)

        # she is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # she types "buy peacock feathers" into a text box
        # edith ties fishing lures for fun

        # when she hits enter the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # there is still a textbox inviting her to add another item
        # she enters "User peacock feathers to make a fly" edith is methodical

        # the page updates again, showing both items in the list

        # satisifed, she goes back to sleep

if __name__ == "__main__":
    unittest.main()
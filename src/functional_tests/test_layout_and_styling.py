from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # edith goe to the home page
        self.browser.get(self.live_server_url)

        # her browser window is set to a very specific size
        self.browser.set_window_size(1024,768)

        # she notices the input box is nicely centered
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10,
        )

        # she starts a new list and sees the input is nicely centered there too
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: testing")
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertAlmostEqual(
            inputbox.location["x"] + inputbox.size["width"] / 2,
            512,
            delta=10,
        )
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormAutomate:
    """_summary_
    class to automate the form filling
    
    """
    def __init__(self, driver_path):
        """_summary_

        Args:
            path (string): path of the chrome driver (Chrome version: 106.0.5249.119)
            check the chrome version in chrome://settings/help
            get the driver from here: https://chromedriver.chromium.org/downloads
        """
        option = webdriver.ChromeOptions()
        option.add_argument("-incognito")
        option.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.browser = webdriver.Chrome(executable_path= driver_path, options=option)
        self.wait = WebDriverWait(self.browser, 10)
        
    def get_button(self, xpath):
        """_summary_

        Args:
            xpath (string): xpath of the element in the page

        Returns:
            object: selenium button object
        """
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    def open_browser(self, link):
        """_summary_

        Args:
            link (string): link of the page to open
        """
        self.browser.get(link)

    def click_buttons(self, buttons):
        """_summary_

        Args:
            buttons (list): buttons to be clicked
        """
        
        for button in buttons:
            button.click()
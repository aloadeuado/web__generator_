from config import *
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Google.google import *

class app :
    def __init__(self):
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument('--user-data-dir=C:\\drivers\\appdata_chrome\\data')
        options.add_argument('--profile-directory=Default')

        self.driver = webdriver.Chrome(driver, chrome_options=options)
        self.driver.get("https://accounts.google.com/signup")

        self.google_self = google(self.driver)



if __name__ == "__main__":
    app()
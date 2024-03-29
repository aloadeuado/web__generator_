import sys
import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from Data.PersonData import *
from Util.DateStringExtensions import DateStringExtensions


class google:
    def __init__(self, driver):
        self.url = "https://accounts.google.com/signup"
        self.driver = driver
        self.person = createPerson()
        self.putNameAndLastName()
        time.sleep(2)
        self.putBirdDay()
        time.sleep(2)
        self.putSelectEmail()

    def show_exceptions(self, e):
        print(e)
        self.driver.quit()
        sys.exit()
    
    def putNameAndLastName(self):
        name = self.person.name.first or ""
        last_name = self.person.name.last or ""

        self.driver.find_element_by_id("firstName").send_keys(name)
        time.sleep(2)
        self.driver.find_element_by_id("lastName").send_keys(last_name)
        time.sleep(2)
        self.driver.find_element_by_id("collectNameNext").click()

    def putBirdDay(self):

        extensions = DateStringExtensions(str(self.person.dob.date))

        self.driver.find_element_by_id("day").send_keys(extensions.build_document_day_string())
        time.sleep(2)
        self.driver.find_element_by_id("year").send_keys(extensions.build_document_year_string())
        time.sleep(2)
        Select(self.driver.find_element_by_id("month")).select_by_index(extensions.build_document_month_string())
        time.sleep(2)
        Select(self.driver.find_element_by_id("gender")).select_by_index(extensions.build_document_gender(self.person.gender or "female"))
        time.sleep(2)
        self.driver.find_element_by_id("birthdaygenderNext").click()
        time.sleep(2)

    def putSelectEmail(self):

        self.driver.find_element_by_id("selectionc2").click()
        time.sleep(2)
        self.driver.find_element_by_id("selectionc2").click()
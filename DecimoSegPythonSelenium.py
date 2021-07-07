from os import close, name
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from selenium.webdriver.ie.options import ElementScrollBehavior
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, select
import time

class Prueba_9(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_boton_radio(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("How To Create a Custom Checkbox", driver.title)
        time.sleep(3)
        boton_radio = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[4]")
        boton_radio.click()
        time.sleep(3)
        boton_radio = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/input[3]")
        boton_radio.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
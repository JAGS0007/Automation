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
from selenium.webdriver import ActionChains
import time
import cv2

class Prueba_14(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Archivo_exe_de_un_py(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/default.asp")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("HTML Tutorial", driver.title)
        time.sleep(5)
        encontrar1 = driver.find_element_by_css_selector('a.w3-blue')
        encontrar1.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
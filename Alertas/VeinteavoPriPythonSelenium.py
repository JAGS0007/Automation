from os import close, name
from re import I
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from selenium.webdriver.ie.options import ElementScrollBehavior, Options
from selenium.webdriver.chrome.options import Options
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

class Prueba_18(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Alert_Simple(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("File:///C:/Users/ING/Desktop/Automation/Automation/Alertas/AlertSimple.html")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Alerta Simple", driver.title)
        time.sleep(3)
        Alerta_Simple = driver.find_element_by_xpath("/html/body/button")
        Alerta_Simple.click()
        time.sleep(3)
        Alerta_Simple = driver.switch_to_alert()
        Alerta_Simple.dismiss()
        time.sleep(3)

if __name__ == '__main__':
	unittest.main()
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
import pytesseract
import posixpath
import HtmlTestRunner

class Prueba_27(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    #Validar el titulo
    def test_assertNotEqual(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertNotEqual("Google1", driver.title, "El titulo de la pagina es igual")
        time.sleep(3)
    
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ING\\Desktop\\Selenium\\Reportes\\Reporte de pruebas'))
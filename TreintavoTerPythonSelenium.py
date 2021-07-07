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

    #Manejo de pestañas
    def test_Nueva_Pestaña(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Google", driver.title)
        siguiente = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
        siguiente.click()
        print("El id siguiente es:\n", self.driver.current_window_handle)
        Manejo = self.driver.window_handles
        i = 1
        for Manejos in Manejo:
            self.driver.switch_to.window(Manejos)
            print("La pagina ", i," es:\n", self.driver.title)
        time.sleep(3)
    
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
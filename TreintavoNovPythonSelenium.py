from os import close, name
from re import I
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains, keys
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

class Prueba_33(unittest.TestCase):
    def setUp(self) -> None:
        #chromeOptions = Options()
        #chromeOptions.add_experimental_option("prefs",  {
        #    "download.default_directory" : "C:\Users\ING\Desktop\Selenium"
        #})
        self.driver=webdriver.Chrome(ChromeDriverManager().install())#, chrome_options=chromeOptions)
        #return super().setUp()

    def test_Descargar_Archivo(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Tryit Editor v3.6", driver.title)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[7]/div[4]/div/div/iframe"))
        driver.find_element_by_xpath("/html/body/p[2]/a").click()
        #print("Satisfactorio", Movimiento)
        time.sleep(5)
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
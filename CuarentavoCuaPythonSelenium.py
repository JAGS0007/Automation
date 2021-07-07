from os import close, name, sep
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

class Prueba_38(unittest.TestCase):
    def setUp(self) -> None:
        PROXY = "<160.19.232.85:80>"
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
        }
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver=webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        return super().setUp()

    #Proxy
    def test_Proxy(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Google", driver.title)
        time.sleep(5)
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
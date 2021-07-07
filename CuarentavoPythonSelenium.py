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
import keyboard
import pyautogui

class Prueba_34(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())#, chrome_options=chromeOptions)
        #return super().setUp()

    def test_LogIn_PHP(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://tfs.logyca.com:4443/tfs/LogycaCollection/Logyca.MercadoPago")
        time.sleep(5)
        keyboard.write("jesalcedo")
        #print("Satisfactorio")
        time.sleep(2)
        pyautogui.press("tab")
        #print("Satisfactorio")
        time.sleep(2)
        keyboard.write("GrupoLogyca281")
        #print("Satisfactorio")
        time.sleep(2)
        pyautogui.press("enter")
        #print("Satisfactorio")
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("tfs.logyca.com", driver.title)
        time.sleep(10)
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
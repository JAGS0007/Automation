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

class Prueba_32(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    #Buscar Iframe o frame
    def test_Iframe_Frame(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Google", driver.title)
        Click = self.driver.find_element_by_xpath("//*[@id='gbwa']")
        Click.click()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[3]/iframe"))
        Click2 = self.driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/ul[1]/li[4]/a/div/span")
        Click2.click()
        #print("Satisfactorio", Movimiento)
        time.sleep(5)
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
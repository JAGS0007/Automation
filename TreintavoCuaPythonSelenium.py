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

class Prueba_28(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    #Manejo de pestañas
    def test_Movimiento_Mouse(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.ulibertadores.edu.co/estudiantes/")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Estudiantes | Fundación Universitaria Los Libertadores", driver.title)
        Mouse = self.driver.find_element_by_xpath("//*[@id='menu-item-91829']/a[1]")
        Mouse1 = self.driver.find_element_by_xpath("//*[@id='menu-item-92306']/a[1]")
        Movimiento = ActionChains(self.driver)
        #print("Satisfactorio")
        Movimiento.move_to_element(Mouse).move_to_element(Mouse1).click().perform()
        #print("Satisfactorio")
        time.sleep(5)
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
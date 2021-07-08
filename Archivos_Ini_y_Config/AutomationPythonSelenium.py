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
import configparser

class Prueba_Automatica(unittest.TestCase):
    def setUp(self) -> None:
        configuracion = configparser.ConfigParser()
        configuracion.read('C:\\Users\\ING\\Desktop\\Automation\\Automation\\Archivos_Ini_y_Config\\configuracion.ini')
        configuracion.sections()
        ObtenerExplorador = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']
        self.driver = webdriver.Chrome(executable_path = ObtenerExplorador)
        return super().setUp()

    def test_Cokies(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5) # segundos
        driver.get(self.page)
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Google", driver.title)
        navegador = driver.find_element_by_class_name("q")
        print("El resultado:\n", navegador)
        time.sleep(3)
    
    def tearDown(self) -> None:
        self.driver.quit()
        return super().tearDown()

if __name__ == '__main__':
	unittest.main()
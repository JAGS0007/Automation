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
from selenium.common.exceptions import WebDriverException
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
import time
import cv2
import pytesseract
import posixpath
import HtmlTestRunner

class Prueba_39(unittest.TestCase):
    def setUp(self) -> None:
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver=webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        return super().setUp()

    #Cortar una imagen
    def test_Cortar_Imagen(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Google", driver.title)
        time.sleep(2)
        imagen = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/img")
        imagen_encontrada = imagen.location
        tamaño = imagen.size
        G_imagen = driver.get_screenshot_as_png()
        imagen2 = Image.open(BytesIO(G_imagen))
        left = imagen_encontrada['x']
        top = imagen_encontrada['y']
        right = imagen_encontrada['x'] + tamaño ['width']
        boton = imagen_encontrada['x'] + tamaño ['height']
        imagen2 = imagen2.crop((left, top, right, boton))
        imagen2.save('Mi_logo_prueba.png')
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
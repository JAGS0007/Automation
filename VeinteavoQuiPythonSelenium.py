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

class Prueba_20(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Texto_Imagen(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.facebook.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Facebook - Inicia sesión o regístrate", driver.title)
        driver.save_screenshot("img2.png")
        time.sleep(3)
        img2 = cv2.imread("img2.png")
        pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\ING\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
        print("hasta aqui funciona")
        texto = pytesseract.pytesseract.image_to_string(img2)
        print("hasta aqui funciona")
        print("El texto de la imagen es:\n", texto)

if __name__ == '__main__':
	unittest.main()
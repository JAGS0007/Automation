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

class Prueba_25(unittest.TestCase):
    def setUp(self) -> None:
        #En este momento solo manejare el driver de Chrome
        self.cdriver=webdriver.Chrome(ChromeDriverManager().install())
        #El driver de explorer no lo e montado pero se maneja igual que chrome
        #self.edriver=webdriver.Ie()
        return super().setUp()

    #Suite de pruebas con reporte
    def test_Cokies(self):
        cdriver = self.cdriver
        cdriver.maximize_window()
        cdriver.get("https://www.w3schools.com/html/default.asp")
        print("Titulo de la aplicación: ", cdriver.title, "\n")
        print("URL de la aplicación: ", cdriver.current_url, "\n")
        self.assertIn("HTML Tutorial", cdriver.title)
        all_cokies = cdriver.get_cookies()
        print("El resultado:\n", all_cokies, "\n")
        time.sleep(3)
    
    def test_Scroll(self):
        cdriver = self.cdriver
        cdriver.maximize_window()
        cdriver.get("http://www.amazon.com.co")
        print("Titulo de la aplicación: ", cdriver.title, "\n")
        print("URL de la aplicación: ", cdriver.current_url, "\n")
        self.assertIn("Amazon", cdriver.title)
        time.sleep(3)
        cdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    def test_Elementos_En_Tablas(self):
        cdriver = self.cdriver
        cdriver.maximize_window()
        cdriver.get("https://www.w3schools.com/html/html_tables.asp")
        print("Titulo de la aplicación: ", cdriver.title, "\n")
        print("URL de la aplicación: ", cdriver.current_url, "\n")
        self.assertIn("HTML Tables", cdriver.title)
        time.sleep(3)
        valor = cdriver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
        print("El resultado por elemento es: ", valor, "\n")
        time.sleep(3)
        rows = len(cdriver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        col = len(cdriver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
        print("El resultado por elemento es: ", rows, "\n")
        print("El resultado por elemento es: ", col, "\n")
        print("El resultado es: ")
        for n in range(2, rows+1):
            for b in range(1, col+1):
                dato = cdriver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
                print(" - ", dato, end="      ")
                print()
    
    def tearDown(self) -> None:
        self.cdriver.quit()
        #la siguiente linea es para cerrar el driver de explorer
        #self.edriver.quit()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\ING\\Desktop\\Automation\\Automation\\Reportes\\Reporte Suit de pruebas Selenium'))
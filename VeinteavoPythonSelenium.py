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

class Prueba_17(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Elementos_En_Tablas(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.w3schools.com/html/html_tables.asp")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("HTML Tables", driver.title)
        time.sleep(3)
        valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
        print("El resultado por elemento es: ", valor)
        time.sleep(3)
        rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        col = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
        print("El resultado por elemento es: ", rows)
        print("El resultado por elemento es: ", col)
        print("El resultado es: ")
        for n in range(2, rows+1):
            for b in range(1, col+1):
                dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
                print(" - ", dato, end="      ")
                print()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
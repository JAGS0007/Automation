from os import close, name
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from selenium.webdriver.ie.options import ElementScrollBehavior
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class Prueba_5(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Funcion_Implicit_Wait(self):
        driver = self.driver
        driver.implicitly_wait(15) #pausa segundo
        driver.get("http://www.facebook.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Facebook - Inicia sesión o regístrate", driver.title)
        myDinamicElement = driver.find_element_by_name("email")
        print("Funciona", myDinamicElement)
        time.sleep(3)
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
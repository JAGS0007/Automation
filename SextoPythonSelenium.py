from os import close, name
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.ie.options import ElementScrollBehavior
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class Prueba_3(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Navegar_Entre_Paginas(self):
        driver=self.driver
        driver.get("http://www.gmail.com")
        #time.sleep(3)
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Gmail", driver.title)
        time.sleep(3)
        driver.get("http://www.google.com")
        #time.sleep(3)
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Google", driver.title)
        time.sleep(3)
        driver.get("http://www.youtube.com")
        #time.sleep(3)
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("YouTube", driver.title)
        time.sleep(3)
        driver.back()
        #print("FUNCIONA")
        time.sleep(3)
        driver.back()
        #print("FUNCIONA")
        time.sleep(3)
        driver.forward()
        #print("FUNCIONA")
        time.sleep(3)
        driver.forward()
        #print("FUNCIONA")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
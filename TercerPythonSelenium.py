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

class Prueba_1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()
    
    def test_buscar(self):
        driver=self.driver
        driver.get("http://www.facebook.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Facebook - Inicia sesión o regístrate", driver.title)
        elemento=driver.find_element_by_id("email")
        elemento.send_keys("jimmyguerre")
        clave = driver.find_element_by_id("pass")
        clave.send_keys("Intentemos de nuevo")
        clave.send_keys(Keys.ENTER)
        time.sleep(5)
        assert "No se encontro el elemento: " not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
from os import close, name
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

class Prueba_16(unittest.TestCase):
    def setUp(self) -> None:
        #Chrome_options = Options()
        #Chrome_options.add_argument("--headless") #Esto es para ejeutar un proceso en segundo plano pero esta incompleto
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Ejecutar_en_segundo_plano(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Google", driver.title)
        time.sleep(5)
        palabra_busqueda = 'Sele'
        elemento = driver.find_element_by_name('q')
        elemento.send_keys(palabra_busqueda)
        time.sleep(3)
        #print("funciona")
        for i in range(1, 11):
            #print("funciona")
            elementos = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
            print("La busqueda es: ", elementos)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
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

class Prueba_18(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Confirm_Alert(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("File:///C:/Users/ING/Desktop/Selenium/Alertas/PromptAlert.html")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Codigo para prompt Alerta", driver.title)
        time.sleep(3)
        Confirmar_Alerta = driver.find_element_by_xpath("/html/body/button")
        Confirmar_Alerta.click()
        time.sleep(3)
        Confirmar_Alerta = driver.switch_to_alert()
        Confirmar_Alerta.dismiss()#boton de cancelar o recharzar
        time.sleep(3)
        Confirmar_Alerta = driver.find_element_by_xpath("/html/body/button")
        Confirmar_Alerta.click()
        time.sleep(3)
        Confirmar_Alerta = driver.switch_to_alert()
        Confirmar_Alerta.accept()#boton de aceptar
        time.sleep(3)


if __name__ == '__main__':
	unittest.main()
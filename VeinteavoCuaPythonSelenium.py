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

class Prueba_19(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_Notificacion_box(self):
        Opciones = Options()
        #enviar argumentos 1 = permitir notificacion, 2 = bloquear notificacion
        Opciones.add_experimental_option("prefs",{
            "profile.default_content_setting_values.notifications" , 2
        })
        driver = self.driver
        driver.maximize_window()
        driver.get("http://developer.mozilla.org/es/docs/web/API/notification")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Notification - Referencia de la API Web | MDN", driver.title)
        time.sleep(3)
        

if __name__ == '__main__':
	unittest.main()
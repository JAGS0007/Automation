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
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, select
import time

class Prueba_8(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_select(self):
        driver = self.driver
        driver.implicitly_wait(15) #pausa segundo
        driver.maximize_window()
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("How To Create Custom Select Menus", driver.title)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_elements_by_tag_name("option")
        #print("Funciona")
        time.sleep(3)
        for option in opcion:
            print("Los Valores Son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(1)
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()
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

    def test_Navegar_Entre_Pestañas(self):
        driver=self.driver
        driver.get("http://www.google.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Google", driver.title)
        #time.sleep(3)
        driver.execute_script("window.open('');")
        #print("FUNCIONA")
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        #print("FUNCIONA")
        driver.get("http://www.google.com")
        print("Titulo de la aplicación: ", driver.title)
        print("URL de la aplicación: ", driver.current_url)
        self.assertIn("Google", driver.title)
        #print("FUNCIONA")
        #time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        #print("FUNCIONA")
        #time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main()

#elemento=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        
        #elemento.send_keys("selenium", Keys.ARROW_DOWN)
        
#xpath es una estructura de objetos
#xpath relativo //*[@id="input"]
#nodo 
#xpath absoluto /html/body/ntp-app//div[1]/ntp-realbox//div/input
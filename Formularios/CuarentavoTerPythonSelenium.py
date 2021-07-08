from os import close, name, sep
from re import I
from socket import if_nameindex
from typing import List
import unittest
from unittest.main import main
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains, keys
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
from openpyxl import load_workbook
import time
import cv2
import pytesseract
import posixpath
import HtmlTestRunner

class Prueba_37(unittest.TestCase):
    def setUp(self) -> None:
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver=webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        return super().setUp()

    #Llenar un formulario con base de datos excel
    def test_Importar_Excel_Web(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("C:\\Users\\ING\\Desktop\\Automation\\Automation\\Formularios\\FormularioExcel.html")
        time.sleep(5)
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Formulario Automatizado", driver.title)
        time.sleep(5)
        documento = "C:\\Users\\ING\\Desktop\\Automation\\Automation\\Formularios\\DatosAutomatizado.xlsx"
        wb = load_workbook(documento)
        hojas = wb.get_sheet_names()
        print(hojas)
        nombre = wb.get_sheet_by_name("Base de Datos 1")
        print(nombre)
        wb.close()
        for i in range(1,5):
            nomb, apell, edad = nombre[f'A{i}:C{i}'][0]
            print("Nombre:\t", nomb.value, "Apellido:\t", apell.value, "Edad:\t", edad.value)
            time.sleep(1)
            driver.find_element_by_id("nom").send_keys(nomb.value)
            time.sleep(1)
            driver.find_element_by_id("ape").send_keys(apell.value)
            time.sleep(1)
            driver.find_element_by_id("edad").send_keys(edad.value)#en caso de no funcionar colocar str(edad.value)
            time.sleep(1)
            driver.find_element_by_id("enviar").click()
            time.sleep(1)
            print("---Datos enviados")
    
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
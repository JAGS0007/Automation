from os import close, name, sep
from re import I
from socket import if_nameindex
from sys import displayhook
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
from selenium.common.exceptions import WebDriverException
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
import time
import cv2
import pytesseract
import posixpath
import HtmlTestRunner

class Prueba_40(unittest.TestCase):
    def setUp(self) -> None:
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        #chromeOptions.add_argument("--headless")#Realizar automatizaciones en segundo plano
        #self.driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions, options=chromeOptions)
        self.driver=webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        return super().setUp()

    #Portal de viajes
    def test_Portal_De_Viajes(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.bestday.com.mx")
        print("Titulo de la aplicación: ", driver.title, "\n")
        print("URL de la aplicación: ", driver.current_url, "\n")
        self.assertIn("Best Day - Agencia de Viajes: Vuelos, hoteles, paquetes", driver.title)
        time.sleep(2)

        #Ciudad de origen
        cdorigen = driver.find_element_by_xpath("//*[@id='sboxContainer-packages']/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div/input")
        cdorigen.send_keys("Bogotá, Bogotá D.C., Colombia")
        time.sleep(2)
        cdorigen.send_keys(Keys.TAB)
        time.sleep(2)

        #Ciudad de Destino
        cddestino = driver.find_element_by_xpath("//*[@id='sboxContainer-packages']/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/input")
        cddestino.send_keys("Barranquilla, Atlántico, Colombia")
        time.sleep(2)
        cddestino.send_keys(Keys.TAB)
        time.sleep(2)

        #DatePicker1 - ida
        datapicker = driver.find_element_by_xpath("//*[@id='sboxContainer-packages']/div/div/div[3]/div[2]/div[3]/div/div[1]/div/input")
        datapicker.click()
        subirmes = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[2]")
        subirmes.click()
        subirmes.click()
        subirmes.click()
        selectdia1 = driver.find_element_by_xpath("/html/body/div[5]/div/div[5]/div[5]/div[4]/span[16]/span[1]")
        selectdia1.click()
        time.sleep(2)

        #DatePicker2 - vuelta
        selectdia2 = driver.find_element_by_xpath("/html/body/div[5]/div/div[5]/div[5]/div[4]/span[23]/span[1]")
        selectdia2.click()
        time.sleep(2)

        #Aplicar DatePicker's
        aplicar = driver.find_element_by_xpath("/html/body/div[7]/div/div[6]/div[2]/button[2]/em")
        aplicar.click()
        time.sleep(5)

        #Quitar anuncio promocional
        Alerta = driver.find_element_by_id("onesignal-slidedown-dialog")
        Alerta.click()
        NoGracias = driver.find_element_by_css_selector("#onesignal-slidedown-cancel-button")
        NoGracias.click()
        time.sleep(10)
        
        #Seleccionar Habitacion
        habitacion = driver.find_element_by_xpath("//*[@id='sboxContainer-packages']/div/div/div[3]/div[2]/div[5]/div")
        habitacion.click()
        time.sleep(5)

        #Seleccionar Adultos
        AdultosMas = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div:nth-child(1) > div._pnlpk-itemRow__item._pnlpk-stepper-adults.-medium-down-to-lg > div > a.steppers-icon-right.sbox-3-icon-plus")
        #AdultosMenos = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div:nth-child(1) > div._pnlpk-itemRow__item._pnlpk-stepper-adults.-medium-down-to-lg > div > a.steppers-icon-left.sbox-3-icon-minus")
        AdultosMas.click()
        AdultosMas.click()
        #AdultosMenos.click()
        #AdultosMenos.click()
        time.sleep(3)

        #Seleccionar Menores
        MenoresMas = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div:nth-child(2) > div._pnlpk-itemRow__item._pnlpk-stepper-minors.-medium-down-to-lg > div > a.steppers-icon-right.sbox-3-icon-plus")
        #MenoresMenos = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div:nth-child(2) > div._pnlpk-itemRow__item._pnlpk-stepper-minors.-medium-down-to-lg > div > a.steppers-icon-left.sbox-3-icon-minus.-disable")
        MenoresMas.click()
        MenoresMas.click()
        #MenoresMenos.click()
        #MenoresMenos.click()
        time.sleep(5)

        #Seleccionar Edad menor Solo si ahi menores
        #Para cada campo de menor de edad debe inspeccionar campo a campo
        EdadMenor1 = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div._pnlpk-minors-age-select-wrapper > div:nth-child(1) > div._pnlpk-itemRow__item._pnlpk-select-minor-age > div > div > select > option:nth-child(6)")
        time.sleep(2)
        try:
            EdadMenor1.click()
            print("Si se ejecuto")
            time.sleep(2)
        except WebDriverException as e:
            print("No se ejecuto el evento")
            print(e)
            time.sleep(2)
            return (116)
        EdadMenor2 = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel-scroll > div._pnlpk-panel__blocks._pnlpk-dynamicContent > div:nth-child(1) > div._pnlpk-itemBlock__itemRows > div._pnlpk-minors-age-select-wrapper > div._pnlpk-itemRow._pnlpk-minor-age-select._pnlpk-minor-age-select-last-item > div._pnlpk-itemRow__item._pnlpk-select-minor-age > div > div > select > option:nth-child(19)")
        EdadMenor2.click()
        time.sleep(5)

        #Aplicar Habitaciones
        aplicar2 = driver.find_element_by_css_selector("body > div.distpicker.distpicker-rooms-packages.sbox-v4-components > div > div._pnlpk-panel__footer.-medium-down-to-lg > a._pnlpk-apply-button.sbox-3-btn.-primary._pnlpk-panel__button--link-right.-lg")
        aplicar2.click()
        time.sleep(5)

        #Buscar
        Buscar = driver.find_element_by_xpath("//*[@id='sboxContainer-packages']/div/div/div[3]/div[2]/div[6]/div")
        Buscar.click()
        time.sleep(30)

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    #reporte
	unittest.main()
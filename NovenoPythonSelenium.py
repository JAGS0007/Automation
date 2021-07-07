from os import close, name
import posixpath
from socket import if_nameindex
from typing import Counter, List
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
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import cv2

class Prueba_6(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        return super().setUp()

    def test_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        #driver.set_window_position(0, 0)
        #driver.set_window_size(1366, 768)
        driver.save_screenshot("img2.png")
        time.sleep(3)

    def test_Comparando(self):
        #print("hasta aqui funciona")
        img1 = cv2.imread("img1.png")
        #print("hasta aqui funciona")
        img2 = cv2.imread("img2.png")
        #print("hasta aqui funciona")
        #PARA COMPARAR LAS IMAGENES DEBES SER DE IGUAL TAMAÑO Y DE MISMA CALIDAD o el mismo Screenshot pero editado
        diferencia = cv2.absdiff(img1, img2)
        #print("hasta aqui funciona")
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
        #print("hasta aqui funciona")
        contour,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #print("hasta aqui funciona")

        for c in contour:
            if cv2.contourArea(c) >= 20:
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)
                cv2.rectangle(img1,(posicion_x, posicion_y),(posicion_x + ancho, posicion_y + alto),(0,0,255),2)
            
        while(1):
            cv2.imshow('Imagen1', img1)
            cv2.imshow('Imagen2', img2)
            cv2.imshow('Diferencia detectada', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()

if __name__ == '__main__':
	unittest.main()
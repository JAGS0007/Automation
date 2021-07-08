from appium import webdriver
import unittest
import time

class Prueba_1(unittest.TestCase):

    def test_Conexion_Calculadora(self):
        driver = {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "a70q",
            "automationName": "Appium",
            "appPackage": "com.sec.android.app.popupcalculator",
            "appActivity": ".Calculator"
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
        time.sleep(5)
        
if __name__ == '__main__':
    #reporte
	unittest.main()
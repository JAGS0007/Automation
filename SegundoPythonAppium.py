from appium import webdriver
import unittest
import time

class Prueba_2(unittest.TestCase):

    def test_Suma_En_Calculadora(self):
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

        #Suma de dos numeros
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_02").click()
        time.sleep(2)
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_add").click()
        time.sleep(2)
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_08").click()
        time.sleep(2)
        driver.find_element_by_id("com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal").click()
        time.sleep(5)

if __name__ == '__main__':
    #reporte
	unittest.main()
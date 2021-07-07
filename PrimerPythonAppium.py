from appium import webdriver

driver = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "a70q",
    "automationName": "UiAutomator1",
    "appPackage": "com.sec.android.app.popupcalculator",
    "appActivity": ".Calculator"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
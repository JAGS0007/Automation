from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.gmail.com")
print("Titulo de la aplicación: ", driver.title)
print("URL de la aplicación: ", driver.current_url)
User = driver.find_element_by_name("identifier")
User.send_keys("jimmyguerre@gmail.com")
User.send_keys(Keys.ENTER)
time.sleep(30)
password = driver.find_element_by_id("pass")
password.send_keys("Intentemos de nuevo")
password.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
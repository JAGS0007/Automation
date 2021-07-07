from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver=webdriver.Chrome(executable_path=r"C:\dchrome\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.facebook.com")
print("Titulo de la aplicación: ", driver.title)
print("URL de la aplicación: ", driver.current_url)
usuario = driver.find_element_by_id("email")
usuario.send_keys("jimmygue12@hotmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(30)
clave = driver.find_element_by_id("pass")
clave.send_keys("Intentemos de nuevo")
clave.send_keys(Keys.ENTER)
time.sleep(10)
driver.close()
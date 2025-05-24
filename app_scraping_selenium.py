from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

options = Options()
options.add_experimental_option("detach", True)



driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')


driver.get("http://localhost:5000/login.html")

input_element = driver.find_element(By.ID, "caja_email")
input_element.send_keys("jaimeretamal47@gmail.com")

input_element2 = driver.find_element(By.ID, "caja_clave")
input_element2.send_keys("jaime")

input_element3 = driver.find_element(By.ID, "button_registro").click()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 



options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')

resp = driver.get('http://localhost:5000/login.html')

const = driver.find_element(By.XPATH, '//*[@id=caja_email]')
const.send_keys("jaimeretamal47@gmail.com")

const2 = driver.find_element(By.XPATH, '//*[@name=clave]')
const2.send_keys("jaime")

const3 = driver.find_element(By.XPATH, '//*[@id="button_registro"]').click()








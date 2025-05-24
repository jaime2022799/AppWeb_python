
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


driver.get("http://localhost:5000/index.html")


input_element4 = driver.find_element(By.ID, "nombre")
input_element4.send_keys("Daniel")

input_element5 = driver.find_element(By.ID, "apellido")
input_element5.send_keys("Mendoza")

input_element6 = driver.find_element(By.ID, "tipo_evento")
input_element6.send_keys("Consulta")

input_element7 = driver.find_element(By.ID, "Contacto")
input_element7.send_keys("228496895")

input_element8 = driver.find_element(By.ID, "direccion")
input_element8.send_keys("PuenteAlto")

input_element9 = driver.find_element(By.ID, "Email")
input_element9.send_keys("jaimeretamal47@gmail.com")

input_element10 = driver.find_element(By.ID, "submit").click()
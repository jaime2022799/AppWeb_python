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

link_cotizador = driver.find_element(By.ID, "link_cotizador").click()
#driver.find_element(By.CLASS_NAME, "cotizador").click()

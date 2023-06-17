from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os
from selenium.webdriver.common.by import By


chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1366, 784",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


driver.get('https://dgsmtt.aduacademy.in/')
time.sleep(10)

driver.find_element(by=By.XPATH, value='//*[@id="txtLoginId"]').send_keys('mike93122@gmail.com')
time.sleep(4)



driver.find_element(by=By.XPATH, value='//*[@id="txtPassword"]').send_keys('0F851284')
time.sleep(5)

 
driver.find_element(by=By.XPATH, value='//*[@id="loginform"]/button').click()
time.sleep(10)


driver.find_element(by=By.XPATH, value='//*[@id="frmstudenthome"]/fieldset/div[1]/div/span[1]').click()

time.sleep(10)


driver.find_element(by=By.XPATH, value='//*[@id="ninext"]').click()
time.sleep(100)



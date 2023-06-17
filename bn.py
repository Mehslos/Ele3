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

rand_name = names.get_first_name(gender='male')
S = random.randint(4,8)
rn = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))    
names=(rand_name+rn)
ran = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase + string.digits, k = S))    
main= (rand_name+ran+'@gmail.com')
main2 = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(random.randint(8,12))))



driver = webdriver.Chrome()
#driver.fullscreen_window()
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


driver.find_element(by=By.XPATH, value='//*[@id="tretoc"]/div/ul/ul/ul[2]/ul[4]/li[3]/span').click()
time.sleep(1200)

driver.find_element(by=By.XPATH, value='//*[@id="tretoc"]/div/ul/ul/ul[2]/ul[4]/li[4]/span').click()
time.sleep(1600)


driver.find_element(by=By.XPATH, value='//*[@id="tretoc"]/div/ul/ul/ul[2]/ul[4]/li[5]/span').click()
time.sleep(1400)


driver.find_element(by=By.XPATH, value='//*[@id="tretoc"]/div/ul/ul/ul[1]/ul[1]/li[1]/span').click()
time.sleep(1500)

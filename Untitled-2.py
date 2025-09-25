from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.vivo.com/bd/products')
time.sleep(10)
first_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(10)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if first_height == new_height:
        break
    first_height = new_height
elements = driver.find_elements(By.CLASS_NAME, 'product-item-link')
model_names = [ e.get_attribute('data-name') for e in elements ]
df = pd.DataFrame(model_names)
df.to_csv('C:/Users/User/Desktop/vivo_models.csv',index=False)
driver.quit()
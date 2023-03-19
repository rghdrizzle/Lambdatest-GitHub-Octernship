import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Firefox()
driver.get("https://www.lambdatest.com/")
driver.implicitly_wait(3)

try:
    exit_pop=driver.find_element(by=By.ID, value="exit_popup_close")
    exit_pop.click()
except:
    print("no such element found")

header2 = driver.find_element(by=By.LINK_TEXT,value="Enterprise")
header2.click()
time.sleep(2)


header5 = driver.find_element(by=By.LINK_TEXT,value="Pricing")
header5.click()
time.sleep(2)

try:
    exit_pop=driver.find_element(by=By.ID, value="exit_popup_close")
    exit_pop.click()
except:
    print("no such element found")

test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")

log_file = open("netlog.json", "w") 
for item in test: 
  json.dump(item,log_file,indent=6)
  print(item)

log_file.close()

driver.quit()
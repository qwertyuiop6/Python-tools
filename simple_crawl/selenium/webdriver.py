from selenium import webdriver
import sys

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# driver.service.stop()
# driver.quit()
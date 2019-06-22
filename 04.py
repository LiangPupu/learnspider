from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/baidu?wd=%E7%BE%8E%E5%A5%B3')
driver.find_element_by_partial_link_text('柳岩').click()
time.sleep(1)
driver.quit()
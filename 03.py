from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('美女')
driver.find_element_by_id('su').click()
time.sleep(1)
driver.save_screenshot('./img/baidu.png')
text = driver.find_element_by_id('u1').text
print(text)

print(driver.title, driver.get_cookies())

driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys('高冷')
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(1)
driver.save_screenshot('./img/baidu2.png')
driver.quit()
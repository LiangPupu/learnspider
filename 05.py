from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://www.douban.com/')
frame1 = d.find_element_by_tag_name('iframe')
time.sleep(3)
d.switch_to.frame(frame1)
d.find_element_by_class_name('account-tab-account ').click()
d.find_element_by_id('username').send_keys('18111111111')
d.find_element_by_id('password').send_keys('1234444')
d.find_element_by_class_name('account-form-field-submit ').click()
d.save_screenshot('./img/douban.png')
d.quit()


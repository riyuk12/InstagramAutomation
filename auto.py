#user:chotariyuk,pass:
#explorexpath://*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a
#username input: //*[@id="loginForm"]/div/div[1]/div/label/input
#password input: //*[@id="loginForm"]/div/div[2]/div/label/input
#not now class: aOO1W HoLwm
#explore elements://*[@id="react-root"]/section/main/div/div[1]/div
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path=r"C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(path)

driver.get("https://www.instagram.com")
time.sleep(3)
user=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user.send_keys('chotariyuk')
time.sleep(1)
pas=user=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys('rajatbose10')
time.sleep(1)
button=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
button.click()
time.sleep(5)
notnow=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notnow.click()
time.sleep(7)
notnow=driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
notnow.click()
time.sleep(3)
explore=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
explore.click()
time.sleep(3)
page=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div')
print(page.text)
time.sleep(10)
driver.quit()

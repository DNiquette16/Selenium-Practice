from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("/Users/Dannyniquette/Documents/chromedriver")
driver.get("https://www.youtube.com")
driver.switch_to_window(driver.current_window_handle)
sleep(1)
class1 = driver.find_element_by_xpath("//*[@id='text']").click()
user = driver.find_element_by_xpath('//*[@id="identifierId"]')

user.send_keys("EMAIL")
nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
sleep(3)
pword = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pword.send_keys("PASSWORD")
nextButton2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
sleep(4)

Rec1 = driver.find_element_by_xpath('//*[@id="video-title"]').text
Rec1_name = driver.find_element_by_xpath('//*[@id="byline"]/a').text
print("First recommended video is: ", Rec1, "posted by", Rec1_name)
sleep(10)
driver.quit()

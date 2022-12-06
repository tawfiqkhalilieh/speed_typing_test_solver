# the test: https://typing-speed-test.aoeu.eu/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://typing-speed-test.aoeu.eu/")

input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"[id='input']"))
)

input.click()
for i in range(300):
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[id='currentword']"))
    )
    input.send_keys(element.text)
    input.send_keys(" ")

time.sleep(20)

print("\nSpeed typing finished successfully!\n")
browser.quit()
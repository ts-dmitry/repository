from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    x_element.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    input1 = input1.text

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(calc(input1))

    x_element = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    x_element.click()

finally:
    time.sleep(5)
    browser.quit()
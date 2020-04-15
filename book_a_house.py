from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    btn=browser.find_element_by_xpath("//button[@id='book']")
    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, ('price')),'$100'))
    btn.click()
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    result = browser.find_element_by_xpath("//input[@id='answer']")
    Submit_btn = browser.find_element_by_xpath("//button[text()='Submit']")
    
    x = x_element.text
    y = calc(x)
    result.send_keys(y)
    Submit_btn.click()

    alert = browser.switch_to.alert
    print(alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

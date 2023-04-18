from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "/Users/b31/Documents/class/chromedriver" # 드라이버의 경로를 지정합니다.
browser = webdriver.Chrome(executable_path=driver_path)

url = "https://finance.naver.com"
browser.get(url)

datas = browser.find_elements(By.CLASS_NAME, 'num_quot')

for elem in datas:
  print(elem.text, "\n")

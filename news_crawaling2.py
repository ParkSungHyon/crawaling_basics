from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver_path = "/Users/b31/Documents/class/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259"
browser.get(url)

news = browser.find_elements(By.CLASS_NAME, 'type06_headline')
news_a = news.find_elements(By.TAG_NAME, 'a') # 제목
news_link = browser.find_elements(By.CLASS_NAME, 'type06_headline').get_attribute('href')
news_lede = news.find_elements(By.CLASS_NAME, 'lede') # 내용
news_wr = news.find_elements(By.CLASS_NAME, 'writing') # 신문사


for i in news_a:
      print(i.text)
      
for i in news_lede:
      print(i.text)
   
for i in news_a:
      print(i.get_attribute('href'))

for i in news_wr:
      print(i.text)


#news_a_list = []
#news_link = []
#news_lede_list = []
#news_wr_list = []

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver_path = "/Users/b31/Documents/class/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=101&sid2=259"
browser.get(url)

#####attribte를 호출하기 위해서는 같은 < > 안에 있어야 한다.
### 같은 페이지에서 반복 횟수는 어떻게 정하나?

news = browser.find_element(By.CLASS_NAME, 'content')
news_a = news.find_elements(By.TAG_NAME, 'a') # 제목
news_lede = news.find_elements(By.CLASS_NAME, 'lede') # 내용
news_wr = news.find_elements(By.CLASS_NAME, 'writing') # 신문사

title = []
summary = []
link = []
company = []


for i in news_a:
    title.append(i.text)
    
for i in news_lede:
    summary.append(i.text)
       
for i in news_a:
    link.append(i.get_attribute('href'))

for i in news_wr:
    company.append(i.text)

for i in range(0,20):
    print(f"제목{i} : " + title[i])
    print("내용 : " + summary[i])
    print("링크 : " + link[i])
    print("신문사 : " + company[i] + "\n")
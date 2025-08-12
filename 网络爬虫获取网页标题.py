import requests
from bs4 import BeautifulSoup

# 要爬取的网页URL，起点读书
uri = "https://www.qidian.com/"

# 发送请求获取网页内容
response = requests.get(uri)
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, "himl.parser")
    # 获取网页标题
    title = soup.title.string
    print(f"该网页的标题是：{title}")
else:
    print(f"请求网页失败，状态码：{response.status_code}")







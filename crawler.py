# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req      
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Requrest Headers 的資訊   # 找尋 Request Headers 請參考 "https://www.youtube.com/watch?v=9Z9xKWfNo7k&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=19&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B"
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

# 解析原始碼，取得每篇文章的標題
import bs4                    # pip install beautifulsoup4
root = bs4.BeautifulSoup(data, "html.parser")    # "html.parser" 告訴程式是 html
#print(root.title.string)   # 抓取 html 裡的 title 標籤   # string 是指抓取文字，也可以不要加

#titles = root.find("div", class_="title")  # 尋找 class="title" 的 div 標籤
#print(titles.a.string)     # .a 的用意為找尋 a 標籤， .string 表示為只要文字

titles = root.find_all("div", class_="title")  # 尋找所有 class="title" 的 div 標籤
for title in titles:
    if title.a != None:   # 如果標題包含 a 標籤 (沒有被刪除)，印出來
        print(title.a.string)

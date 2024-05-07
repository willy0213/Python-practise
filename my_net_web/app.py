from flask import Flask
app = Flask(__name__)      #  __name__ 代表目前執行的模組名稱

@app.route('/')      # 函式的裝飾 (decorator): 已函式為基礎，提供附加的功能
def home():
    return 'Hello Flask 2'

@app.route("/test")   # 代表我們要處理的網站路徑
def test():
    return "This is Test"

if __name__ == '__main__':      # 如果以主程式執行
    app.run()                   # 啟動 Flask 伺服器
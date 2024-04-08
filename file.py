#儲存檔案 part1 英文
file=open('data0.txt',mode='w')          #開啟
file.write("Hello file")                #操作1
file.write("Hello file\nSecond Line")   #操作2  
file.close()                            #關閉

#儲存檔案 part2 中文
file=open('data1.txt',mode="w",encoding='utf-8')   #如果要使用中文，需要增加 encoding 並且編碼格式為 utf-8 即可使用中文
file.write("測試中文\n好棒棒")
file.close()

#儲存檔案 part3 數字 較好的寫法
with open("data2.txt",mode="w",encoding='utf-8') as file:
    file.write("5\n3" )                            #不用寫 close 程式會自動關閉檔案


#讀取檔案 part1 英文
with open("data0.txt",mode='r') as file:
    data=file.read()
print(data)

#讀取檔案 part2 中文
with open("data1.txt",mode='r',encoding="utf-8") as file:
    data=file.read()
print(data)

#讀取檔案 part3 數字     #把檔案中的數字資料，一行一行讀取出來，並計算總合
sum=0
with open("data2.txt",mode='r',encoding="utf-8") as file:
    for line in file:                                      #一行一行的讀取
        sum+=int(line)
print(sum) 

#使用 JSON 格式讀取，複寫檔案
import json 
with open("config.json",mode="r") as file:
    data=json.load(file)     #data 是一個字典資料
print("name ",data["name"])
print("version ", data['version'])

#從檔案中讀取 JSON 資料，放入變數 data 裡面 
with open("config.json",mode="r") as file:
    data=json.load(file)     
print(data)                 #data 是一個字典資料
data['name']='new name'     #修改變數中的資料   
#把最新的資料複寫回檔案中
with open("config.json",mode='w') as file:
    json.dump(data,file)
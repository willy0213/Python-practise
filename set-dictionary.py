#集合的運算 part1
s1={3,4,5}
print(3 in s1)      #True
print(10 in s1)     #False
print(10 not in s1) #True

#集合的運算 part2
s1={3,4,5}
s2={4,5,6,7}

s3=s1&s2     #交集:取兩個集合中，相同的資料  
print(s3)    #{4,5}

s3=s1|s2     #聯集:取兩個集合中的所有資料，但不重複取
print(s3)    #{3,4,5,6,7}

s3=s1-s2     #差集:從s1中，減去和s2重疊的部分，這個是有順序的
print(s3)    #{3}

s3=s1^s2     #反差集:取兩個集合中，不重疊的部分
print(s3)    #{3,6,7}

#集合的運算 part3
s=set("Hello")  #set(字串)
print(s)     #會印出hello所有的字母，且沒有順序性的印出來
print("H" in s)  #True 
print("a" in s)  #False

#字典的運算: key-value
dic={"apple":"蘋果","bug":"蟲蟲",}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic['apple'])

#字典的運算: 判斷key是否存在於dic
dic={"apple":"蘋果","bug":"蟲蟲",}
print("apple" in dic)  #判斷key是否存在  #True
print("test" in dic)   #False
print("test" not in dic)  #True

#字典的運算: 鍵值對刪除
dic={"apple":"蘋果","bug":"蟲蟲",}
print(dic)        #{'apple': '蘋果', 'bug': '蟲蟲'}
del dic["apple"]  #刪除字典中的鍵值對(key-value pair)
print(dic)        #{'bug': '蟲蟲'}

#字典的運算:
dic={x:x*2 for x in [3,4,5]}  #固定格式語法(for 代號 in 列表)，X為列表中的數字去創造鍵值對
print(dic)    #{3:6,4:8,5:10}
 










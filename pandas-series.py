# 載入　pandas 模組
import pandas as pd

# 資料索引
data = pd.Series([5, 4, -2, 3, 7], index=['a', 'b', 'c', 'd', 'e'])
print(data)

# 觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料總和", data.index)

# 取得資料: 根據順序或根據索引
print(data[2], data[0])
print(data["e"], data["d"])

# 數字運算: 基本, 統計, 順序
print("最大值:", data.max())
print("標準差:", data.std())
print("平均值:", data.mean())
print("總和:", data.sum())
print("全部相乘:", data.prod())
print("中位數:", data.median())
print("最大的三個數字:", data.nlargest(3))
print("最小的兩個數字:", data.nsmallest(2))

# 建立字串資料
data1 = pd.Series(["您好", "Python", "Pandas"])
print(data1)

# 字串運算: 基本, 串接, 搜尋, 取代
print("算出字串長度:", data1.str.len())
print("全部變小寫:", data1.str.lower())
print("全部變大寫:", data1.str.upper())
print("全部串接(,):", data1.str.cat(sep=","))
print("全部串接(-):", data1.str.cat(sep="-"))
print("搜尋字串中是否包含 'P':\n",data1.str.contains("P"))
print("取代字串中 'P' 為 'X':\n" ,data1.str.replace("P", "X"))

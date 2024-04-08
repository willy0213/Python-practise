# break 的簡單範例
n=0
while n<5:
    if n==3:
        break  #直接跳出這個迴圈
    print(n)   #印出迴圈中的 n ,012
    n+=1
print("最後的 n: ",n)   #印出最後的 n ,3

# continue 的簡易範例
n=0
for x in [0,1,2,3]:
    if x%2==0:      #x 是偶數
        continue    #跳出這次迴圈重新執行下一圈
    print(x)
    n+=1
print("最後的 n: ",n)

# else 的簡單範例
sum=0
for n in range(11):
    sum+=n
else:
    print(sum)    #印出 1+2+.....+10 的結果

# 綜合範例: 找出整數平方根    # 輸入9,得到3    # 輸入11.得到[沒有]整數平方根
n=int(input("輸入一個正整數: "))
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break     # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
        print("沒有整數平方根")
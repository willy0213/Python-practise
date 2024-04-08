#數字運算
x=3+6
print(x)
y=3/6
print(y)
z=3//6  #整數除法，不會除到小數點
print(z)
a=2**3 #2的3次方
print(a)
b=2**0.5 #2的開根號
print(b)
c=7%3 #取餘數
print(c)
x+=1 #x=x+1 #將變數中的數字+1
print(x)

#字串運算
s="Hello"  #單雙引號都可以
print(s)
d="Hell\"o" #跳脫(\)
print(d)
e="Hello"+"World"
print(e)
f="Hello" "World"  #空白也可以代表串接
print(f)
g="Hello\nWodld"   #換行使用\n
print(g)
h="""Hello         
world"""           #使用三個"""也可以呈現換行的結果
print(h)
i="Hello"*3+"World"  #可以使Hello重複3次
print(i)

#字串會對內部的字元編號(索引)，從0開始算起
j="Hello"
print(j[0])
print(j[1:4]) #取1以後，不包含4
print(j[1:])  #從1算取，取到全部
print(j[:4])  #不算4，前面全部算
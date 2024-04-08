#參數的預設資料  part1
def power(base,exp=0):
    print(base**exp)  #平方為**
power(3,2)            #如果有給定2個值，那麼就不會使用預設資料exp=0，3^2=9
power(4)              #如果只有給定1個值，那麼就會使用預設資料exp=0，4^0=1


#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)    #可以直接給參數資料，只要在前面加上參數名稱，即可不用管順序

# 無限/不定 參數資料
def avg(*ns):              #記得要加*
     sum=0
     for n in ns:
         sum=sum+n
     print(sum/len(ns))    #len代表序列的長度
avg(3,4)
avg(3,5,10)
avg(1,4,-1,-8)

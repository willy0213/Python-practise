#定義類別，與類別屬性(封裝在類別中的變數和函式)
#定義一個類別 IO，有兩個屬性 supporttedSrcs 和 read
class IO:
    supportedSrcs=["console","flie"]
    def read(src):
        print("Read from",src)
#使用類別
print(IO.supportedSrcs)
IO.read("flie")


#定義一個類別 IO，有兩個屬性 supporttedSrcs 和 read
class IO:
    supportedSrcs=["console","flie"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from",src)
#使用類別
print(IO.supportedSrcs)
IO.read("flie")
IO.read("internet")


#定義一個類別 IO，有一個屬性 supporttedSrcs
class IO:
    supportedSrcs=["console","flie"]
  
#使用類別
print(IO.supportedSrcs)

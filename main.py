#封包
#在封包資料夾裡裡面一定要有 __init__.py 這個檔案，否則無法成為封包
#範例為建立一個 geometry 的資料夾，在裡面放封包 
#格式為: import 封包名稱 函式名稱

#主程式
import geometry.point
result=geometry.point.distance(3,4)
print(result)

import geometry.line
result=geometry.line.slope(1,1,3,3)
print("斜率", result)

import geometry.line as line
result=line.len(1,1,3,3)
print(result)
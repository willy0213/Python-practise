#載入內建的 sys 模組並取得資訊 part1
import sys
print(sys.platform)   #作業系統
print(sys.maxsize)

#載入內建的 sys 模組並取得資訊 part2
import sys as s
print(s.platform)
print(s.maxsize)

#建立 geometry 模組，載入使用
sys.path.append("modules")           #在模組的搜尋路徑列表中[新增路徑]
import geometry                      # import 自己建立的模組
result=geometry.distance(1,1,5,5)    
print(result)
result=geometry.slope(1,2,5,6)
print(result)

#調整搜尋模組的路徑
import sys
print(sys.path)    #印出模組的搜尋路徑
import geometry
print(geometry.distance(1,1,5,5,))

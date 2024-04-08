#while 迴圈 part1
n=1
while n<=3:
    print(n)
    n+=1

#while 迴圈 part2
n=1
sum=0  #紀錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)

#for 迴圈 part1
for x in [3,5,1]:
    print(x)

for y in "Hello":
    print(y)

for z in range(5):
    print(z)

for w in range(5,10):   #包含5不包含10
     print(w)

#for 迴圈 part2
sum=0
for a in range(11):
    sum=sum+a
print(sum)
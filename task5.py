"""
DAY:thursday
DATE:8th dec 2022
TOPIC:task
AUTHOR:pooja
"""
#not to display continue
n=0
while(n<10):
    n+=1
    if n==6:
        continue
    print(n) #1 to 10
  #retrieve only negatives
n=[5,10,15,20,-4,-3,-1,0,8]
for i in n:
    if(i<0):
        print(i)  #-4 -3 -1

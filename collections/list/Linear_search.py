#LINEAR SEARCH ALGORITHM
#Time complexity is high
#iteration = number of elements
lst=[1,4,6,7,8,15,20,5,2,3]

#read element from console
flag=0
check_the_num=int(input("Give the Number :"))
for i in lst:
    if(i==check_the_num):
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("not found")



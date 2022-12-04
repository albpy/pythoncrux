#1.
lst = [1,5,6,7,8,9,10]

print(lst[-0]+lst[5]) #lst[0]=1+9=10

#2.
#read element from console==>6
#pairs to get 6 from lst ===>(1,5)
"""a=0
b=1
for i in lst:
    if i<6:
        pair1=lst[a]
        pair2=lst[b]
        pair1+pair2=6
        a+=1
        print(pair1,pair2)
        break"""
lst1=[15,5,4,20,10,3]
a=0
lst2=[]
#get lst2=[42,52,53,37,47]
for i in lst1:
   result=sum(lst1)-lst1[a]
   lst2.append(result)
   a+=1
print(lst2)


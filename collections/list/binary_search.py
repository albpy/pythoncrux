#1.sort the given list [ascending order]
lst=[1,4,3,5,10,8,9]
lst.sort()
low=0
flag=0
upp=len(lst)-1 #6
element=int(input("enter the check_number :"))
while (low<=upp):
#mid
#mid=low+upp//2 = 0+6//2=3
    mid=(low+upp)//2 #3
    
#  condition lst[3]
   #1.searching>lst[mid]  #(9>5)
     #low=mid+1
    if element>lst[mid]:
        low=mid+1 #low=3
   #2.searching<lst[mid]  #(3<5)
    elif element<lst[mid]:
        upp=mid-1
        
    #3.searching=lst[mid] element found
    elif element==lst[mid]:
        flag=1
        break
if (flag>0):
    print("Found")
else:
    print("Not found")



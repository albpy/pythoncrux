tu=(10,20,30,40,50,60,70,80,90,100)

#Q)Update the value of 50==>75
#tuple is immutable
lst=[]
for i in tu:
    lst.append(i)
lst[4]=75
print(lst)

#convert to tuple
tu=tuple(lst)
print(tu)

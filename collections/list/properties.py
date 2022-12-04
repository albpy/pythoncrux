#1.How to define(Method 1)

lst=[] # empty list
print(type(lst))

        #Method 2
lst1=list() #list function
print(type(lst1))


#2.Heterogeneous supported or not-->Supported

lst2=[10,10.5,'bigdata','python',123456789,True,False]
#10.5-->Float,123456789-->Long/Biginit,True/False-->Boolean
print(lst2)

#3.Duplicate allowed or not -->Allowed

lst3=[1,2,2,3,1,5,5,5,17,17,9,8]
print(lst3)

#4.Insertion order is preserved

#5.Mutable or immutable --> Mutable

lst4=[15,20,25,30,35,40,45,50,55,60,65,70]
      #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11
print(lst4[3]) #index 0 to (n-1)
print(lst4)
#update 25 --> 100
lst4[2]=100
print(lst4)
lst4[3]='bigdata'
print(lst4)

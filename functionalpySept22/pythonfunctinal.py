#polymorphism 
#Abstraction----------Seminar Topics
#-----------------------------Functional--------------------------------
"""fuctions are used to reussablity of code and reduce the length of program
#1.lambda               |
#2.map                  |
#3.filter               |
#4.list-comprehension   |       ----These are functions of functional programm

1.lambda ===> lambda is the anonymous function"""

f=lambda num1,num2:num1+num2

print(f(10,30))
    #No declartion of function,No Need to def,No Name of function
"""
2.Map &&  filter==>not focus on syntax got confused  but where to use
"""
#[1,2,3,4,5,6,7,8,9,10]===>f(x)===>[1,4,9,16,25,36,49,64,81,100] 
"""Eg:Calculate the square of all elements and add to new list"""
#Normal program to apped square all functions
squarelist=[1,2,3,4,5,6,7,8,9,10]
newsqre=[]
for i in squarelist:
    newi=i**2
    newsqre.append(newi)
print(newsqre)

#------------------------------Using map-------------------------------
#syntsx===>variablename=list(map(arguement1,arguement2))
"""arguement1 is the name of the function==>function name
   arguement2 is the name of list===>iterable name"""
lst=[1,2,3,4,5]
def square(num):
    return num**2
sqreMap=list(map(square,lst))
print(sqreMap)
#Map usin lambda
LambdaMap=list(map(lambda num:num**2,lst))
print(LambdaMap)


"""filter===> collect/Apllied to  specified(conditionalised)  elements
eg: cllect even nuumber
filter===>[1,2,3,4,5]===>f(x)==>[2,4]"""
#Syntax==>Variablename=list(filter(fn,iterable)
FindEven=list(filter(lambda num:num%2==0,lst))
print(FindEven)


"""4.list-comprehension
-----List comprehension is used to reduce program in list----
                    3 Methods are there"""


#Add 1 - 50 elements to a list

#Normal method
lssst=[]
for i in range(1,51):
    lssst.append(i)
print(lssst)

#-----------list-comprehension----------
"""Method 1"""
#syntax [print range]
lsst=[i for i in range(1,16)]
print(lsst)


"""Method 2"""
#collect even numbers from 1to50
#syntax==>[print range if confition]
eve1to50=[i for i in range(1,51) if i%2==0]
print(eve1to50)


#Nested_list

lst=[[101,'vinay','k',26,'bigdata',1000],
        [102,'amal','k',27,'python',1250],
        [103,'arjun','p',29,'bigdata',1500],
        [104,'vivek','p',28,'bigdata',1750],
        [105,'vineeth','p',31,'python',2000],
        [106,'Anonymous','k',32,'coder',2250],
        [107,'lucracious','p',33,'miner',2500]]
#to print each list
#for i in lst:
#    print(i)
#To print ID, first name, lastname,age,prof(proffesion)
#for i in lst:
#    print(i[1],i[2],i[3],i[4])
#    print(i[:5])
#age above 27 fname, lname, age, prof
lst1=[]
for i in lst:
    if i[3]>27:
        print(i[1:5])
#prof bigdata --> fname, age, salary
for i in lst:
    if i[4]=='bigdata':
        print(i[1::2])
#age above 27 and prof python [fname, lname, age, prof]

for i in lst:
     if i[3]>27 and i[4=='python']:
         print(i[1:5])

#total salary of 7 employees
sum_=0
for i in lst:
    sum_+=i[5]
print(sum_)


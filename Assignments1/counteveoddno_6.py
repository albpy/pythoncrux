numbers=(1,2,3,4,5,6,7,8,9)
count=0
odd=0
for i in numbers:
    if i%2==0:
        count+=1
    else:
        odd+=1
print("even integers=",count)
print("odd integers =",odd)

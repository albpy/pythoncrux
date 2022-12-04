print(2,3)
lst=[2,3]
for i in range(1,101):
    prime_nos=((6*i)-1)#without 7         #((6*i)+1)==>7 Onwards
    if prime_nos<=100:
        lst.append(prime_nos)
print(lst)

        

lst=[10,11,12,13,14,15,16,17,18,19]

#Calculate the square of odd numbera from the list using functional prgrm
sqreOfodd=list(map(lambda num:num**2,filter(lambda num:num%2!=0,lst)))
print(sqreOfodd)

"""sqreOfoddInvert=list(filter(lambda num:num**2,map(lambda num:num%2!=0,lst)))
print(sqreOfoddInvert)"""

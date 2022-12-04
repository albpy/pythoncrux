string='luminartechnolab'

#vowels lsit print
vowels='aeiou'
lst=[]

lst1=[]
for i in string:
#vowels
    if i in vowels:
        lst.append(i)
     
#non-vowels charecters
    if i not in vowels:
        lst1.append(i)
print(lst)
print(lst1,len(lst1))

#calculate spaces in a sentence
the_string='I work in the pavan cycles and motors'
lst2=[]
for i in the_string:
    if i==' ':
        lst2.append(i)
print(len(lst2))


word=str(input("Enter your word: "))
new_word=""
j=-1
for i in word:
    new_word=new_word+word[j]
    j=j-1
print(new_word)
count=0
for i in new_word:
    if i != word[count]:
        count+=1
        print("not")
        break
    else:
        print("yes palindrome")



    


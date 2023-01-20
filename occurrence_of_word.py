string=input("Enter the string:")
word=input("Enter the word to be searched:")
count=0
for w in word:
    if w == word:
        count=count+1
print("the count of the word in the string is:",count)
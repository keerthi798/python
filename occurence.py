str=(input("enter a string"))
str.lower()
str2=set(str)
for i in str2:
    c=0
    for j in range(len(str)):
       if i==str[j]:
            c=c+1
    print("occurence of", i, c)


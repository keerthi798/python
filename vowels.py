elem= input("Enter the elements : ")
vowels =['a','e','i','o','u']
list1=[]
for x in elem:
    if x in vowels :
        list1.append(x)
print("Vowels present in given statement : ",list1)
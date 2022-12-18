a=int(input("Enter the limit:"))
i=1
sum1=0
sum2=0
while i<a:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
    i=i+1
print("sum of even nos:",sum1)
print("sum of odd nos:",sum2)
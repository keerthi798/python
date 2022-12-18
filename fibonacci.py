list=int(input("enter a limit:"))
n1=0
n2=1
count=0
print("fibonacci series is :")
while count<list:
    print(n1)
    N=n1+n2
    n1=n2
    n2=N
    count=count+1

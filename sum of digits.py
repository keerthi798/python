n=float(input("Enter a number:"))
t=0
while(n>0):
    dig=n%10
    t=t+dig
    n=n//10
print("The total sum of digits is:",t)
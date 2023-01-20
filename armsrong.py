n=int(input("enter a nuber"))
sum = 0
temp = n
while n != 0:
    rec = n % 10
    sum = sum + rec * rec * rec
    n = n // 10

if temp == sum:
       print("armstrong no")
else:
      printf("not an armstrong ")
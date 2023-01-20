num = int(input("Enter a number:"))
n = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        n = 1
        break
    i = i + 1

if n == 0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")
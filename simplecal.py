print("1.ADD")#simple calculator
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
choice=input("enter the your choice: \t")
if choice =='1':
    num1=int(input("\nenter the first number:"))#input two values
    num2=int(input("\nenter the second number:"))
    print("\nThe result is:\t",(num1+num2))#addition
elif choice =='2':
     num1 = int(input("\nenter the first number"))
     num2 = int(input("\nenter the second number"))
     print("The result is:\t", (num1 - num2))#subtraction
elif choice =='3':
     num1 = int(input("\nenter the first number"))
     num2 = int(input("\nenter the second number"))
     print("The result is:\t", (num1*num2))#multiplication
elif choice =='4':
    num1 = int(input("\nenter the first number"))
    num2 = int(input("\nenter the second number"))
    print("The result is:\t",(num1 / num2))#divion of two numbers
else:
    print("default ")

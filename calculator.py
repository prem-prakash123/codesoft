num1=int(input("Enter the first number:-"))
num2=int(input("Enter the second number:-"))
operation=input("Select the Operation(+,-,*,/):")

if operation == "+":
    print(num1+num2)

elif operation == "-":
    print(num1-num2)

elif operation == "*":
    print(num1*num2)

elif operation == "/":
    print(num1/num2)

else:
    print("Invalid operation")

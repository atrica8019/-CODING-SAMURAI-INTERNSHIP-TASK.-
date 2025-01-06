#CALCULATOR
num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
op= input("Enter the operation you want to perform \n '+','-','*','/' : ")

if op=='+':
    result = num1+num2
elif op=='-':
    result = num1-num2
elif op == '*':
    result = num1 - num2
elif op=='/':
    result = num1 / num2
    if num2 == 0:
        print("Invalid Operand")

else:
    print("Not Applicable")

print(f"The result is: {result}")


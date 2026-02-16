#Stage1
num1 = float(input("enter first number:-"))
num2 = float(input("enter second number:-"))
op= input("enter operator(+,-,*,/)")
if op == '+':
    result = num1+num2
    print("result = {result}")
elif op == '-':
    result = num1-num2
    print ("result = {result}")
elif op == '*':
    result = num1*num2
    print("result = {result}")
elif op == '/':
    if num2 !=0:
      result = num1/num2
      print("result = {result}")
    else:
      print("division by xero not allowed")
else:
   print("Invalid input")


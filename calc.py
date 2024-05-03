"""CALCULATOR"""

num1 = int (input ("enter the first  number :- "))
num2 = int (input(" enter the second number :- "))
op =  input ("enter the operation :- ")
if op == "+":
    result = num1 + num2
    print(result)
elif op == "-" :
    result = num1 - num2 
    print(result)
elif op == "*":
    result = num1 * num2
    print (result)
else : 
    result = num1 / num2 
    print (result)      


        
    
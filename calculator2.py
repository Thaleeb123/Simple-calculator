"""calculator"""
print("1 - add")
print("2 - sub")
print("3 - multiply")
print("4 - divide")
print("integers only")
option = int(input("choose the operation"))
num1 = int(input("enter the first number:-"))
num2 = int(input("enter the second number:-")) 
if(option == 1):
        result= num1 + num2
        print(result)
elif (option ==2):
        result = num1 - num2
        print(result)
elif (option == 3):
        result = num1 * num2
        print(result)
elif (option== 4):
        result = num1 // num2 
        print(result)
else:
     print("invalid option")
         
           

#Calculator
#Program make a simple calculator

def add(x, y):
   return x + y

def sub(x, y):
   return x - y
   
def mul(x, y):
   return x * y
   
def div(x, y):
   return x / y

x=float(input("Enter num1 : "))
#print(x)
y=float(input("Enter num2 : "))
#print(y)

choice=input('Enter choice of operator : ')

if choice == '+':
   print(x,"+",y,"=", add(x,y))

elif choice == '-':
   print(x,"-",y,"=", sub(x,y))

elif choice == '*':
   print(x,"*",y,"=", mul(x,y))

elif choice == '/':
   print(x,"/",y,"=", div(x,y))

else:
    print('Enter valid choice among + - * /')

#Largest number among the three inputs

print("Enter 3 numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 > num2) and (num1 > num3):
  largest = num1
elif(num2 > num3):
  largest = num2
else:
  largest = num3
  
print("Largest number is ",largest)

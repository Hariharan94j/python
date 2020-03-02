# Palindrome number

num = int(input("Enter Number: "))
temp = num
rev = 0
while(temp > 0):
  rem = temp %10
  rev = (rev *10) + rem
  temp = temp //10
#print("Reverse = ", rev)
if(num == rev):
  print(num,"is a palindrome number")
else:
  print(num,"is not a palindrome number")\

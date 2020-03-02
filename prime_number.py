#Prime number

num=int(input("Enter number : "))
flag=1
div=int(num/2)

for i in range(2,div):
  x=num%i
  if(x==0):
    flag=0
    i=div
  else:
    i-=1
    
if(flag==0):
  print(num,"is not prime")
else:
  print(num,"is a prime")

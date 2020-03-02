#Fibbonacci series

count=int(input("Number of Fibbonacci numbers : "))
first=0
second=1

for i in range (0,count):
  if(i<=1):
    nxt=i
  else:
    nxt=first+second
    first=second
    second=nxt
  print(nxt)
  i-=1

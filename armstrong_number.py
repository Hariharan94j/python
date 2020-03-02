#Armstrong number
#if 407 is a number, its armstrong is (4^3 + 0^3 + 7^3 = 64 + 343 = 407) is True
#if 25 is a number, its armstrong is (2^3 + 5^3 = 8 + 125 = 133) is False

num=int(input("Enter number : "))
temp=num
ams=0;

while(temp!=0):
  rem = temp%10
  ams = ams + (rem*rem*rem)
  temp = temp//10

print("Armstrong :",ams)

if(ams == num):
  print(num,"is an Armstrong number")
else:
  print(num,"is not an Armstrong number")

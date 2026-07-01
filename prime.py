num=int(input("enter a number to calculate prime :"))

flag=False

if (num==0 or num==1):
  print("not a prime number")


for i in range (2,num):
  if (num%i==0):
    flag=True
    break

if flag:
  print("not a prime number")
else:
  print("yes a prime number")
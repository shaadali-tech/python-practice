n=int(input("enter a number : "))

flag=False

if(n==0 or n==1):
  print("enter a valid number")

for i in range(2,n):
  if(n%i==0):
    flag=True
    break

if flag:
  print("not a prime")
else:
  print("yes a prime number")
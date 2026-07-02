# num=int(input("Enter a number"))

# def factorial(num):
#   if num==0 or num==1:
#     return 1
  
#   return num*factorial(num-1)

# fact=factorial(num)
# print(fact)

n=int(input("Enter a number to check prime or not : "))

if (n==0 or n==1):
  print()

flag=False

for i in range(2,n):
  if(n%i)==0:
    flag=True
    break

if flag:
  print("Not a prime number")
else:
  print("yes a prime number")
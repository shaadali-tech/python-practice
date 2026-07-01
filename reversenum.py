num=int(input("Enter a number to reverse :"))

# rev=0
original=num
# while(num>0):
#   digit=num%10
#   rev=rev*10+digit
#   num=num//10

# print(rev)

# if(original==rev):
#   print("number is palindrome")
# else:
#   print("number is not palindrome")

# Armstrong Number

sum=0

while(num>0):
  digit=num%10
  sum=sum+digit**3
  num=num//10

if(original==sum):
  print("number is armstron")
else:
  print("not a armstrong")
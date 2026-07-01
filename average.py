size=int(input("enter the size of an array :"))

lst=[]

for i in range(size):
  num=int(input("enter the element"))
  lst.append(num)

print(lst)
sum=0
for i in lst:
  sum+=i

print(sum)
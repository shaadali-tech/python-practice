n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

lst.sort()

print("Second Largest =", lst[-2])
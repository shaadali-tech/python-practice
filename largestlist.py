n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input())
    lst.append(num)

largest = lst[0]

for i in lst:
    if i > largest:
        largest = i

print("Largest =", largest)
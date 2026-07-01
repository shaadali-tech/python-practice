#program  to check vowel

str=input("Enter a string ")
count=0
vowel="aeiou"

for ch in str.lower():
  if (ch in vowel):
    count+=1
    

print(count)
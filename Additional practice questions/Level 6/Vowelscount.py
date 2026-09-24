n = input("Enter a string: ")
count = 0
#count mtlb counter h
for i in n:
    if i in "aeiouAEIOU":
        count += 1
print("Vowels:", count)
n = input("Enter string: ")
result = ""

for i in n:
    if i not in result:
        result = result + i

print(result)
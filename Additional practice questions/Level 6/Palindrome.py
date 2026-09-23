n= input("string")
reverse =""
for i in n:
    reverse = i + reverse
if reverse == n:
    print("Palindrome")
else:
    print("Not palindrome")

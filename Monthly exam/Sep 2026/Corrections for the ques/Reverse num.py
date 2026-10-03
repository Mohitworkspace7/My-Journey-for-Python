i = int(input("Number"))
digit = 0
rev = 0
while i >0:
    digit = i %10
    rev = rev*10 + digit 
    i = i//10
print(rev)
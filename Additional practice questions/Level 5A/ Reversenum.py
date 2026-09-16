n =int(input("Number "))
rev = 0
while n>0:
    digit = n % 10 #module last num
    rev = rev * 10 + digit #rev = 0 + 10
    n = n // 10 #last vala number hta dega
print(rev)
n = int(input("Number"))
o = n
b=0
while n> 0:
    a = n%10 #extract the digit
    b += a*a*a #store the number and add the other num
    n//=10 #remove the digit
if b == o:
    print("Armstrong")
else:
    print("usual number")
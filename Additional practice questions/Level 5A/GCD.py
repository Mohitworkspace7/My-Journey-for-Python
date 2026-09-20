a=int(input("first number"))
b=int(input("second num"))
c=0
for i in range(1,min(a,b)+1):
    if a % i == 0:
        if b % i == 0:
            c=i
    i+=1
print(c)
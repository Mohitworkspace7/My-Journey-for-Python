n = int(input("Number1"))
m = int(input("number2"))
gcd =0
for i in range(1,min(n,m)+1):
    if n % i == 0:
        if m % i == 0:
            gcd = i
            i+=1
print(gcd)
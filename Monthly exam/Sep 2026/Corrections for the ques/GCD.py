n = int(input("Number1"))
m = int(input("number2"))
gcd =0
if m < n:
    for i in range(1,m+1):
        if m%i==0 and n%i==0:
            gcd = i
            i+=1
    print(gcd)
     
else:
     for j in range(1,n+1):
        if m%j==0 and n%j==0:
            gcd =j
            j+=1
     print(gcd)     
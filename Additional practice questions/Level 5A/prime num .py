n= int(input("Number"))
m=1
for i in range(2,n):
    m = n % i
    i+=1
    if m == 0:
       print("not prime")
       break
else:
    print("Prime")
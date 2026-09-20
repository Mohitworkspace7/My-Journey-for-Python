n= int(input("Number "))
a=0
for i in range(1,n):
    if n%i==0:
        a=a+i 
if a==n:
    print("Perfect num")
else:
    print("usual num")
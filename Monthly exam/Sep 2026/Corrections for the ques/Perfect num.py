n = int(input("Number "))
f = 0
for i in range(1,n):
    if n%i==0:
        f +=i
if f==n:
        print("Perfect number")
else:
        print("Usual Num")
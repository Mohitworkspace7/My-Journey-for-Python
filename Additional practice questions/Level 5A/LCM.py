a=int(input("first number"))
b=int(input("second num"))
c=0 # for hcf/gcd
lcm=0
#the loop for hcf/gcd
for i in range(1,min(a,b)+1):
    if a % i == 0:
        if b % i == 0:
            c=i
    i+=1
lcm = a *b/c # formula for lcm 
print(lcm)
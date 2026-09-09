n = int(input("Factorial of "))
fact = 1
i = 1
#remembee variables define krna bhot jaruri hai
while i <= n:
    #yha loop create kiya mene
    fact *= i
    i += 1
    #*= += ahort way hai fact mai mene i ko multply store kiya h
print (fact)
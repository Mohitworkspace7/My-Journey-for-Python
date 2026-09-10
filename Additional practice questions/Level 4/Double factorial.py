n = int(input("Double factorial "))
fact = 1
if n%2==0:
    for i in range(2,n+1,2):
        fact = fact * i
else:
     for i in range(1,n+1,2):
         fact = fact*i
print(fact)
#here i use if else with for loop
#if else because there are two condition
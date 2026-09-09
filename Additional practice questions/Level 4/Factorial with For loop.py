n = int(input("Factorial of "))
#two variables were created fact ko create krke 1 value assign ki
fact = 1
for i in range(1,n+1):
    #i progressilvely bdega 1 se n tk
    #remember range ka 1 se jo last hoga uska minus 1
    fact = fact * i
    #yha fact mai fact multiply with i store kiya mene
print(fact)
#ab fact prgressively hoga aur nfactorial show krega
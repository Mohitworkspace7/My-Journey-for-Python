lst= [10,20,30,20,40,10,50]
dupli =[]
for i in lst:
    if lst.count(i)> 1 and i not in dupli:
        dupli.append(i)
print(dupli)
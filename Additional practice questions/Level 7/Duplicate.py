lst=[1,2,3,4,5,1]
dupli = []
for i in lst:
    if lst.count(i)>1 and i not in dupli:
        dupli.append(i)
print(dupli)
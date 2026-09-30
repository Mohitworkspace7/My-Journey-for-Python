lst=[1,2,3,4,3,2,5,7]
a =[]
for i in lst:
    if lst.count(i) <=1 and i not in a:
        a.append(i)
print(a)

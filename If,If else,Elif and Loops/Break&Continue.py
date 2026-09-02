#break mtlb pura loop band krna
#jse ye example
for i in range(1,5):
    if i == 3:
        break
    print(i)
#Another example
for i in range(5,50):
    if (i%5 ==0):
        print (i)
    if i == 25:
        break
#Continue mtlb us iteration ya number ko skip kro
for i in range(5,50):
    if i== 25:
        continue
    print(i)
#ye example skip krega 25 baaki 5 se 49 print krega
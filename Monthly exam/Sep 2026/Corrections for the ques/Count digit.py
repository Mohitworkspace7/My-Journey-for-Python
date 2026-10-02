i = int(input("Number"))
count = 0
while i >0:
    i//=10
    count +=1
print(count)
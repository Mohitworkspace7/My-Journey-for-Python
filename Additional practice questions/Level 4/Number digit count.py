num = int(input("Number "))
count = 0
while num > 0:
    num = num//10 #number ke decimal part ko hta deta h
    count+=1
print(count)
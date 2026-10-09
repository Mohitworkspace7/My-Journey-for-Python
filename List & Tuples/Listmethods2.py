lst = [1,2,5,39,6]
lst.insert(1,89) #insert the data in particular index
m =[837,23,28,94]
lst.extend(m)
#is case mai m list lst ke last mai jud jayegi
#agr lst ko khrb nhi krna h to
l = lst + m
print(l)
#for remove of specific value
lst.remove(5)
#iey 5 remove ho jayega
numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)
numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers

print(a)
print(b)
print(c)
#10
#[20, 30, 40]
#50
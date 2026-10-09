# List
a = [10, 20, 30]
a[0] = 100
print(a)  # [100, 20, 30]

# Tuple# immutable
b = (10, 20, 30)
# b[0] = 100  # TypeError
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[2])   # 30
print(t[-1])  # 40
#slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])
#Length
t = (10, 20, 30)
print(len(t))
#count&index
t = (10, 20, 10, 30)

print(t.count(10))  # 2
print(t.index(20))  # 1
#tuple unpackin
person = ("Mohit", 25, "Python")

name, age, skill = person

print(name)
print(age)
print(skill)
#Mohit
#25
#Python
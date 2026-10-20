def add(*args):
    print(args)

add(10, 20, 30)

#. *args se addition
def add(*args):
    total = 0

    for i in args:
        total += i

    return total

print(add(10, 20))
print(add(10, 20, 30, 40))
print(add(5, 5, 5, 5, 5))
#normal argument ke sath
def student(name, *marks):
    print("Name:", name)
    print("Marks:", marks)

student("Mohit", 80, 90, 75)
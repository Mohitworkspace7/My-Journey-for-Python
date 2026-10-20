#Python mein **kwargs ka use function mein multiple keyword arguments ko dictionary ke form mein receive karne ke liye hota hai.
def student(**kwargs):
    print(kwargs)

student(name="Mohit", age=25, city="Delhi")
#acess krna
def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

student(name="Mohit", age=25)
#**kwargs
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Mohit", age=25, course="Python")

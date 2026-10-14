#1. No parameters, no return
def greet():
    print("Hello Mohit")
greet()
#2. Parameters, no return
def square(n):
    print(n * n)
square(5)
#3.Parameters with return
def square(n):
    return n * n
result = square(5)
print(result)
#4.No parameters, with return
def get_number():
    return 100

print(get_number())
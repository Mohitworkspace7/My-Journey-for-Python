
def fact(n):
    result = 1

    while n > 0:
        result *= n
        n -= 1
    print(result)

fact(3)

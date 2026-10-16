def prime(n):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        print("prime")
prime(17)
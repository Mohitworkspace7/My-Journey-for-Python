for i in range(2, 100):
    prime = True#use of boolean

    for n in range(2, i):
        if i % n == 0:
            prime = False
            break
            #break means that it is not a prime number

    if prime:
        print(i)
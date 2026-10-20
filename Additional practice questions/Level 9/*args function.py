def max(*Max):
    m = 0
    for i in Max:
        if i > m :
            m = i
    return m
print(max(1,2,4,5,7))
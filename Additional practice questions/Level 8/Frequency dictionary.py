lst = [1,1,2,4,5,6,6,7,7,8]
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
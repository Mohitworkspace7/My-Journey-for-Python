m = input("String")
word = ""
for i in m:
    if i not in word:
        if word.count(i) <= 1:
            word = word + i
print(word)  
    
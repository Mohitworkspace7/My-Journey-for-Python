Text = input("Write a text")
words = Text.split()
Word_count = {}
for word in words:
    if word in Word_count:
        Word_count[word] += 1
    else:
        Word_count[word] = 1
print(Word_count)
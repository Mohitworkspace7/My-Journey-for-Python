Jab input size n*n￼ badhta hai, toh operations lagbhag n*n ke proportion mein badhte hain.
Example: Ek loop ke andar doosra loop chalana

numbers = [10, 20, 30, 40]

for i in numbers:
    for j in numbers:
        print(i, j)
#Har nested loop O(n²) nahi hota. Agar inner loop fixed number of times chalta hai, toh complexity O(n) bhi ho sakti hai.
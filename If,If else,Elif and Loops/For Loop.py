#For loop sequence ke har item ko ek ek karke repeat krna hota h
for i in range(5):
    print(i)
#output 0,1,2,3,4 hi hoga 5 excluded hoga
#Jse hume 1 se 10 ka print krna h to
for i in range(1,11):
    print(i)
#evene number ke liye
for i in range(2,100,2):
    print(i)
#yaha Range(Start,Stop,Step)
n = int(input("Number="))
for i in range(1,11):
    print(n*i)
#ye multiply ka hai
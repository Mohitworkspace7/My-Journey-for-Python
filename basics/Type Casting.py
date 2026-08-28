#Type casting means casting the type of variable into another 
#like int to float type casting
age = input("Enter your age: ")
print(type(age))
#from this we can find the type
int("25")       # string → integer
float("25.5")   # string → float
str(25)         # integer → string
#another example is
a = "10"
b = "20"
print(int(a) + int(b))
#in this case if we dont use int then it will be strings
#and the output would be 1020
Marks = int(input("Marks obtained by 100 "))
if Marks >= 80:
    print("A+")
elif Marks >= 70 and Marks < 80:
    print("A")
elif Marks >= 60 and Marks < 70:
    print("B+")
elif Marks >= 50 and Marks < 60:
    print("B")
elif Marks >= 33 and Marks < 50:
    print("C")
else:
    print("Fail")
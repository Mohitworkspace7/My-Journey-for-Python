student = {
    "name": "Rahul",
    "marks": 85,
    "age": 20
}

print(student["name"])
print(student["marks"])
print(student.get("name"))
print(student.get("city"))

#new data add
student = {
    "name": "Rahul",
    "marks": 85
}

student["age"] = 20

print(student)
#value update
student = {
    "name": "Rahul",
    "marks": 85
}

student["marks"] = 95

print(student)
#delete krna
student = {
    "name": "Rahul",
    "marks": 85,
    "age": 20
}

x = student.pop("marks")

print(x)
print(student)
#last item delete
student = {
    "name": "Rahul",
    "age": 20
}

print(student.popitem())
#loop lgana
for name in marks:
    print(name)
#By default, dictionary par loop lagane se keys milti hain.
for score in marks.values():
    print(score)
for name, score in marks.items():
    print(name, score)
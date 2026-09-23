d = dict()
print(d)
#simple dictionary create krn
student = dict(name="Mohit", age=25, course="Python")
print(student)
#yha par key and values de rhe hai
#yaha par name key mohit value
#age key 25 value
student = dict(name="Mohit", age=25)
print(student["name"])
print(student["age"])
#yaha value ko access kr rha hu
student.keys()       # keys saari
student.values()     # values saare
student.items()      # key-value pairs saare
student.get("name")  # value safely get karna
student.update(...)  # data add/update
student.pop("age")   # item remove
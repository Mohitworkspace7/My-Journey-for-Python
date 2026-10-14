x = 100  # Global variable
def show():
    print(x)
show()
print(x)
#global variable function ke bahar hota h
def show():
    x = 50  # Local variable
    print(x)
show()
print(x)
#local variable function ke bahara hota h
#isiliye out iteriation vala eroor btayega
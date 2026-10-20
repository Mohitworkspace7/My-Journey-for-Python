# *args aur **kwargs ka main difference hai: *args multiple values leta hai, aur **kwargs named values ko dictionary mein leta hai
#*args = Tuple
#**kwargs = Dictionary
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(10, 20, name="Mohit", language="Python")
#isme output
#Args: (10, 20)
#Kwargs: {'name': 'Mohit', 'language': 'Python'}
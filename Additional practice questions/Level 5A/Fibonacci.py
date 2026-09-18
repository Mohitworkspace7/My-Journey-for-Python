n = 10
a=0
b=1
while n>0:
    print(a)
    c = a + b
    a = b
    b = c
    n-=1
    #here three number are important
    #kyuki hum number ko shift krrhe h
    #a 0 hai sbse phle print hoga phir aai b ki value
    #aur b mai c ki value add ho jayegi
    #aur ye fibonacci way m kaam krenge
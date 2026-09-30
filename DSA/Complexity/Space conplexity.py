#Space Complexity = Algorithm ko run karne ke liye kitni extra memory chahiye.
#example ko lete h
n = 100
#ye big O(1)
#agar koi loop ho toh jaise
for i in range(0,n+1):
    print(i)
#ye big O(n) hoga kyuki n baar value store hori h
for i in range(0,9):
    for j in range(0,i):
        print(j)
#ye big O(n2) ka example h
#Space complexity mein usually auxiliary space 
#yani input ke alawa algorithm ki extra memory ko focus karte hain.
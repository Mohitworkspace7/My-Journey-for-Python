bill = int(input("Bill unit"))
if bill < 100:
    print(bill * 2)
elif bill < 200:
    print(bill * 2 +  (bill - 100) * 3)
#Bill -100 means if unit is 150 then 50 units are for 3
elif bill < 300:
    print(bill * 2 + (bill - 100) * 3 + (bill - 200) * 4)
    #this goes same unit - 200 means 100
else:
    print(bill * 2 + (bill - 100) * 3 + (bill - 200) * 4 + (bill - 300) * 5)
    #this example when above 100 bhi 2 per unit plus 3 bhi ho
    #agr 100-200 mai sirf ek hi ruppe per unit ho toh 100*3 100*2 lekin logical operator bhi lgenge
    #jse and kyuki hum limit kr rhe h ki yhi slab mai vo number aaye
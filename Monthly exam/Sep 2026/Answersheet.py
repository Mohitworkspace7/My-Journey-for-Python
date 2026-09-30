#answer1 = means that you asigm it a value while == means is it equals to the value
#answer2 type casting is to change the type ex are
i= int(input("Number"))
m =float(input("Decimal num"))
#answer3 3 and 1
#answer4 / means divide // means module
#answer5 input to get value print to display value
#answer6 and means both conditions should be true otherwise it will not run
# or means one of the both comditions can be true
# not means the comdition is not true 
#ans7 while loop used for conditions
#for loop it continous loop 
#ans8 break means to break the loop 
#continue means to skip the value
#ans9 strings are character
#a = " mohit" & a = "haish"
#ans10 list is mutable while tuple is immutable
#ans11 A
#ans12 
i = int(input("Number"))
if i >0:
    print("Positive")
elif i<0:
    print("Negative")
else:
    print("Zero")
#ans13 
i = int(input("Number"))
count = 0
while i >=0:
    i=//10
    count +=1
print(count)
#ans14
i = int(input("Number"))
reverse = 0
while i >= 0:
    reverse = i//10
    i =%10
print(reverse)
#ans15
a = int(input("Number"))
b = int(input("Number"))
for i in range(0, max(a,b)):
#ans16
lst= [10,20,30,20,40,10,50]
dupli =[]
for i in lst:
    if count(i)> 1 and i not in dupli:
        dupli.append(i)
print(dupli)
#ans17
lst= [10,20,30,20,40,10,50]
dupli =[]
for i in lst:
    if count(i) < 1 and i not in dupli:
        dupli.append(i)
print(dupli)
#ans18
lst=[1,2,3,4,5,6]
a = max(lst)
lst.remove(a)
b = max(lst)
print(b)
#ans19
#len() means the length of string
#max() return maximum value
#min() return minimum value
#sum() return sum of value
#abs() return absolute or positive value
#ans20
list.append(a) #means we add the value of a in list
list.extend(lst) #means we are merging two lists
list.insert(1,35) #means we are insertinga value in a particukar index
#ans21
a = input("String")
print(a[::-1])
#ans22
a = input("String")
count =0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print(count)
#ans23
a = input("String")
b = ""
for i in a:
    if i not in b and 
    b += i
print(b)
#ans24
a = input("String")
b = input("String")
if sort(a) == sort(b):
    print("Anagrams")
else:
    print("Not anagram")
#ans25
a = int(input("Number"))
b = 0
for i in a:
    if a>=0:
        b = a//10
        a%=10
        c =b *b*b
        c+=c
if c= a:
    print("Perfect number")
#ans26
lst = [10,20,20,15]
dupli= []
for i in lst:
    if count(i) < 1 and i not in dupli:
        dupli.append(i)
a = max(dupli)
dupli.remove(a)
b = max(dupli)
print(b)
#ans27
lst=[1,2,2,3,3,3,4]
for i in lst:
    b = count(i)
    lst.append(b)
#ans28
for i in range(0,100):
    for j in range(0,i):
        if i % j == 0:
            print("not prime")
        else:
            print("Prime")
#ans29
#big (O) notation mtlb kitne easily info process hori h
#example ki O(1) mtlb ek hi baar m output mil rha h
#mtlb kitne attempt m kitna answer mil rha h 
#type O(1),O(n),O(n2),O(logn)
#ans30
#O(n) kyuki n baar loop chal rha h
#ans31
#O(n2) kyuki do baar loop chl rha h
#ans32
#time complexity mtlb kitne loop m example output dera h
#spave complexity mtlb kitni space le rha h output dene m
#ans33
#O(1)
#ans34
i = int(input("Marks"))
lst =[]
lst.append(i)
a = max(lst)
print("Maximum",a)
b = min(lst)
print("Minimum",b)
for j in lst:
    j +=1
    j/=count(j)
print("Average",j)
counter= 0
for k in lst:
    if k > j:
        counter+=1
print("Above average",counter)

    

        
    

    
    
    


    
    

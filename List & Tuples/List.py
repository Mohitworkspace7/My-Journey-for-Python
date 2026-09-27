#list m bhot variables store kr skte h
lst = [1,2,3,4]
#not only one type of variable but also other type of variables bhi
lst = [1,2,3,"B",True]
print(type(lst))
#1st value ko nikalne ke liye
print(marks[0])
#negrive index
print(marks[-1]) #ye last index ki value dega
#similarly -2 second kast ki value dega
#we can also check ki koi value h list m ya nhi
if 2 in marks:
    print("Yes")
#ya hum kahe
if "B" in marks:
    print("Yes")
#agr puri lis chahiye to
print(lst)
print(lst[:])
#yahi se shuru hoti hai list slicing
print(lst[1:4:1])
#yaha par lst [start:stop:step] ka concept ata h
#jaha par stop ki value exculded hoti h hmesa
print(lst[1:4])
#toh ye value dega 2,3, "B"
#nyi list bnate h
marks = [i for i in range(10)]
marks = [ i* i for i in range(10) if i %2 == 0]
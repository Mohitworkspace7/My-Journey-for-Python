#first lets create a lst
lst = [1,8,4,3,7]
#to insert a value
lst.append(9)
#to sort the list
lst.sort()
lst.sort(reverse= True)
lst.reverse()#reverse the original lst
lst.index(8) #index of the value
lst.count(1) #count krega kitni baar aya h value
m = lst
m[0] = 0
print(lst)
#toh ye lst bhi change hogi

#Time complexity means how much time it will take to run code
#across the equation like har chiz/loop se jana hoga answer mai pahuchne ke liye
#yakitne time m milega answer
#it affects the bigger codes
#isey big O m likhte h
#There are different type of time complexity
#first one O(1)
n = [10, 20, 30, 40]
print(n[2])
#yha value fetch krne ke liye sirf ek hi time lga
# O(n)
for i in range(n):
    print(i)
    #jitni value hogi utni baar loop chlega
#O(n²)
for i in range(n):
    for j in range(n):
        print(i, j)
        #double work like har chiz har chiz ke sath match khayegi
# O(n + n) = O(2n) = O(n) 
#O(log n) mtlb kam baar search
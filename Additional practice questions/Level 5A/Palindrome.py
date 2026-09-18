n = int(input("Number"))
rev=0
while n>0:
    digit = n%10
    rev= rev*10 + digit
    n = n//10
if rev == n:
    print("Number is palindrome")
else:
    print("Number is not a palindrome")
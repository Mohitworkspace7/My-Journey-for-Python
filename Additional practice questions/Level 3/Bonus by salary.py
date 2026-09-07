salary = float(input("Enter your salary: "))

if salary < 20000:
    bonus = salary * 0.20
elif salary <= 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus =", bonus)
#if whole salary then it will be
print("Total Salary =", salary + bonus)
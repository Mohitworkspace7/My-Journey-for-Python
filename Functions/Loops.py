def get_even(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result
#list mai even number
nums = [1, 2, 3, 4, 5, 6]
print(get_even(nums))
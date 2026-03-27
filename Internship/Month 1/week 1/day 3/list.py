numbers = [1,2,3,4,5,6,7,8]

even_numbers = []

for num in numbers:
    if num%2 == 0:
        even_numbers.append(num)

print("original list:", numbers)
print("Even numbers list: ", even_numbers)
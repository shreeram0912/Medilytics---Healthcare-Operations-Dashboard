def find_missing_number(arr):
    n = len(arr)+1
    total = n * (n+1) / 2
    return total - sum(arr)

numbers = [1,2,3,4,6]
print("The missing number is:", find_missing_number(numbers))
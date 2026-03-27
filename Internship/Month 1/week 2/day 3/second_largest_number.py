def second_largest_number(nums):
    first = second = float('-inf')

    for num in nums:
        if num>first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second

print(second_largest_number([10,20,32,3,24]))
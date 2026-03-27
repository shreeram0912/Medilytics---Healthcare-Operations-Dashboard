def is_power(num):
    return num > 0 and (num & (num-1)) == 0

num = 17
print(is_power(num))
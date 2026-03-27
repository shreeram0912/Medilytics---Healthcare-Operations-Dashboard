#Array Attributes
import numpy as np

arr = np.array([[10,20,30], [40,50,60]])

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data Type:", type(arr))

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", np.add(a,b))
print("Subtraction:", np.subtract(a,b))
print("Multiplication:", np.multiply(a, b))
print("Division:", np.divide(a, b))

print("Sum:", np.sum(a))
print("Mean:", np.mean(b))
print("Maximum:", np.max(a))
print("Minimum:", np.min(b))
print("Standard Deviation:,", np.std(a))

print("Element 1 in array a:", np.array(a[0]))
print("Element 2 in array b:", np.array(b[2]))
print("Last element in array a:", np.array(a[-1]))

print("Elements from index 0 to 3 in array a:", np.array(a[0:3]))

#2d array to show 1st row second column and all rows second column, from 2nd row first 2 columns

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)
print("\n1st row, 2nd column:")
print(arr[0, 1])
print("\nAll rows, 2nd column:")
print(arr[:, 1])
print("\nFrom 2nd row, first 2 columns:")
print(arr[1:, 0:2])
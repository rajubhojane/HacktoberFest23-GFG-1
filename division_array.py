# Example arrays (lists)
array1 = [10, 20, 30, 40]
array2 = [2, 4, 5, 10]

# Perform element-wise division using list comprehension
result = [a / b for a, b in zip(array1, array2)]
print(result)  # Output: [5.0, 5.0, 6.0, 4.0]

"""
Problem 1: Find the minimum and maximum elements in an array
"""
'''
arr = [45, 78, 90, 32, 67, 89, 33, 54, 78, 34]

# for i in range(len(arr)):
#     print(arr[i])
    # O(n)  n = length of the list/array
    # O(nlogn)  n = length of the array/list

# arr.sort()   # O(nlogn) time complexity

# print("Minimum = ", arr[0], "Maximum = ", arr[len(arr) - 1])

maximum_element = arr[0]
minimum_element = arr[0]

for i in range(len(arr)):
    maximum_element = max(maximum_element, arr[i])
    minimum_element = min(minimum_element, arr[i])
    # if arr[i] > maximum_element:
    #     maximum_element = arr[i]
    # if arr[i] < minimum_element:
    #     minimum_element = arr[i]

print("Minimum = ", minimum_element, "Maximum = ", maximum_element)
'''


"""
Problem 2: Cyclically rotate an array by one
"""
'''
# {1, 2, 3, 4, 5}
# {5, 1, 2, 3, 4}

arr = [1, 2, 3, 4, 5]

# x = arr[len(arr) - 1]  # 5

# for i in range(len(arr) - 1, 0, -1):
#     # start = 4, stop = 0, step = -1
#     # i = 1
#     arr[i] = arr[i - 1]

# # [1, 1, 2, 3, 4]
# arr[0] = x

# i = 0
# j = len(arr) - 1

# while i != j:
#     arr[i], arr[j] = arr[j], arr[i]
#     i += 1

arr = arr[-1:] + arr[:-1]

print(arr)
'''

"""
Problem 3: Find the largest sum of contiguous subarray / Kadane's Algorithm
"""
'''
arr = [-2, -3, 4, -1, -2, 1, 5, -3]

result = arr[0]
sum = 0
start = 0
end = 0

for i in range(len(arr)):
    sum = sum + arr[i]
    if result < sum:
        result = sum
        end = i
    if sum < 0:
        sum = 0
        start = i + 1

print(arr[start: end + 1])
print(result)
'''


"""
Problem 4: Find if an array is a subset of another array
"""
'''
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

temp = set(arr1 + arr2)

if len(temp) == len(arr1):
    print("Is a Subset")
else:
    print("Is not a Subset")
'''


"""
Problem 5: Rotate a matrix by 90 degree
"""

'''

[                     [
[1, 2, 3],            [7, 4, 1],
[4, 5, 6],    -->     [8, 5, 2],
[7, 8, 9]             [9, 6, 3]
]                     ]

[00, 01, 02]
[10, 11, 12]
[20, 21, 22]

[1, 4, 7]
[2, 5, 8]
[3, 6, 9]

'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)

for row in range(len(matrix)):
    for col in range(0, row):
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

print(matrix)

n = len(matrix)
for row in range(n):
    for col in range(n // 2):
        matrix[row][col], matrix[row][n - 1 - col] = matrix[row][n - 1 - col], matrix[row][col]

for row in matrix:
    row = row.reverse()

print(matrix)






























# data = input("Enter the numbers")
# data = data.split(", ")
# # data = '3', '5', '6', '7', '8'

# print("List: ", list(data))
# print("List: ", tuple(data))


# fname = "House of the Dragon.mp4"
# # first, last = fname.split(".")
# name = fname.split(".")
# print(name[-1])

# Concatenation
# n = input("Enter the number: ")
# print("Total: ", (int(n) + int(n + n) + int(n + n + n)))

# import sys
# print(sys.version)

# from datetime import datetime as dt

# dt_now = dt.now()
# print(dt_now)

# date1 = dt(2014, 7, 2)
# date2 = dt(2014, 7, 11)
# print(str(date2 - date1)[0])



# function_library = {
# "abs()": ["abs(number) -> number", "Return the absolute value of the number"],
# "print()": ["print(value) -> value", "Prints the value"],
# "sum()": ["sum(values) -> sum", "Returns the sum of given values"]
# }

# data = input("Enter the function: ")
# required = function_library[data]
# for item in required:
#     print(item)


# import calendar

# print(calendar.month(2022, 9, 3, 3))




# number = int(input("Enter the number: "))

# print(abs(17 - number))



numbers = input("Enter the numbers: ")
numbers = numbers.split(", ")
numbers = [int(x) for x in numbers]
s = sum(numbers)

if (3 * numbers[0] == s):
    print(3 * s)
else:
    print(s)







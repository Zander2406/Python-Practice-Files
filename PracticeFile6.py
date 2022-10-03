def NumberSum(a, b):
    return a + b


def NumberDifference(a, b):
    return abs(b - a)


def randomFunc(a, b):
    # summation, difference, summation - difference
    summation = NumberSum(a, b)
    difference = NumberDifference(a, b)
    return summation - difference


def factorial(num):
    # A function calling itself is called recursion
    # This if statement is base case which means the function would return after this point if a certain condition is satisfied
    if num <= 1:
        return 1
    # 5! = 5 * 4 * 3 * 2 * 1
    return num * factorial(num - 1)


# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# sum = a + b
# print(f"Sum is {sum}")


# x = 34
# y = 89
# diff = y - x
# print(f"Difference is {diff}")


if __name__ == "__main__":
    # a = int(input("Enter number 1: "))
    # b = int(input("Enter number 2: "))
    # # sum = NumberSum(a, b)
    # # print(f"Sum is {sum}")
    # print(f"Random Func = {randomFunc(a, b)}")
    print(factorial(5))


































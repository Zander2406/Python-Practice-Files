# def func1(x, y):
#     print(x + y)



# print("Before Calling the function")
# func1(3.5, 4)
# print("After Calling the function")



# def CelsiusToFahrenheit(temperature):
#     return (temperature * (9 / 5)) + 32


# def FahrenheitToCelsius(temperature):
#     return (temperature - 32) * (5 / 9)


# temp = float(input("Enter the temperature: "))
# choice = int(input("1. C -> F\n2. F -> C\n"))
# if choice == 1:
#     temp = CelsiusToFahrenheit(temp)
# else:
#     temp = FahrenheitToCelsius(temp)

# print(temp)
# if temp >= 50:
#     print("Too hot")


# def factorial(number):
#     # 4! = 4 * 3 * 2 * 1
#     # 4! = 1 * 2 * 3 * 4
#     fact = 1
#     for i in range(2, number + 1):
#         fact = fact * i
#     return fact

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    fact = factorial(num)
    print(fact)















# def gcd(a, b):
#     if b == 0:
#         return a
#     if a == 0:
#         return b
    
#     if a == b:
#         return a
    
#     if a > b:
#         return gcd(a - b, b)
#     return gcd(a, b - a)


# a = 24
# b = 18

# if gcd(a, b):
#     print(f"GCD is {gcd(a, b)}")
# else:
#     print("No GCD")







# numbers = input("Enter the 3 numbers: ")
# numbers = numbers.split(" ")
# numbers = [int(x) for x in numbers]

# if len(numbers) == len(set(numbers)):
#     print(sum(numbers))
# else:
#     print(0)



a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if a - b == 0 or abs(a - b) == 5 or a + b == 5:
    print(True)
else:
    print(False)























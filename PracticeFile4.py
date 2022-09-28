'''a = int(input("Enter number: ")) % 2

if a == 0:
    print("Even")
else:
    print("Odd")'''



# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))

# if a + b > 15 and a + b < 20:
#     print(20)
# else:
#     print(a + b)




# word = input("Enter a string: ")

# if "ls" in word:
#     print(word)
# else:
#     print("ls" + word)


# lst = input("Enter the numbers: ")
# lst = lst.split(", ")
# lst = [int(x) for x in lst]
# lst_count = lst.count(4)
# print(lst_count)


# letter = input("Enter the letter: ")
# vowels = ("a", "e", "i", "o", "u")

# if letter in vowels:
#     print("We have a vowel")
# else:
#     print("We have a consonant")


# lst = input("Enter the elements: ")
# lst = lst.split(" ")  # [Ankit, Singh, First, Last]
# print(lst)
# res = ""
# for element in lst:
#     res += element
# print(res)



from typing import final


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
]

final_list = []

for number in numbers:
    if number < 237:
        if number % 2 == 0:
            final_list.append(number)

print(final_list)


finall_list = []
numbers.sort()

for number in numbers:
    if number > 237:
        break
    if number % 2 == 0:
        finall_list.append(number)

print(finall_list)



















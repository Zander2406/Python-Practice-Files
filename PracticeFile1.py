"""
int
string
float
bool
"""




intvariable = 32
stringvar = "Ankit"
floatvar = 3.45
boolvar = False




stringvar = "This is a random string for test purposes"

# print(stringvar[::-2])

stringvar2 = stringvar[:10]

# print(stringvar)
# print(stringvar2)


# Python list example

# l1 = [32, "Ankit", 'A', 45.677, False, [90, 78, "Swarnava", True], "last element"]

# l1[0] = 42

# l1.append("Test")

l2 = [45, 89, 112, 6354, 11, 2]

l2.remove(112)

l2.sort(reverse=True)
# print(l2)
# print()
# print()
# print()

A = (1, 2, 3, 4, 5, 6, 4, 4)

# print(A.count(4))

testdictionary = {
    "Key": "Value",
    "Ankit": "Singh",
    "Emp Id": 8381,
    41: 56,
    21: "Swarnava"
}

testdictionary["Ankit"] = "Kumar Singh"

# print(testdictionary.keys())
# print(testdictionary.values())

# print(testdictionary.get(21))
# # print(testdictionary.get("Emp Id"))


# var = input("Enter the key: ")

# print(testdictionary.get(var))


mylist = [1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5]

print(mylist)
print(set(mylist))

myset = set(mylist)

for var in myset:
    print(var)
















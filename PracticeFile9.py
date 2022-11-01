# Introduction to classes in Python

"""
First Name   Last Name       Emp ID
 Ankit        Singh          I8381
 Swarnava    Bhattacharya    I8684
"""
#  Traditional Method
"""fname = input("Enter first name: ")
lname = input("Enter last name: ")
empid = input("Enter Emp ID: ")"""



class Employee:
    first_name = None
    last_name = None
    employee_id = None

    def __init__(self, fname = None, lname = None, empid = None):
        self.first_name = fname
        self.last_name = lname
        self.employee_id = empid
    
    def show_name(self):
        print(f"{self.first_name} {self.last_name}")

    def show_empid(self):
        return self.employee_id



"""E1 = Employee()
E1.first_name = "Ankit"
E1.last_name = "Singh"
E1.employee_id = 8381
E2 = Employee()
print(E1.first_name)
print(E2.first_name)"""


E1 = Employee("Ankit", "Singh", 8381)
E2 = Employee("Swarnava", "Bhattacharya", 8684)
# print(E1.first_name)
# print(E2.first_name)
E3 = Employee()
# print(E3.first_name)

# E1.show_name()
# my_empid = E2.show_empid()
# print(my_empid)




"""class Grandfather:
    name = "Grandpa"
    lname = "Something"

    def show_grandfathername(self):
        print(self.name)

class Father(Grandfather):
    name = "Dad"

    def show_fathername(self):
        print(self.name)

class Child(Father):
    name = "Son"

    def show_childname(self):
        print(self.name)
    

childvar = Child()
childvar.show_fathername()
print(childvar.lname)"""





"""class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


S1 = Square(4)
R1 = Rectangle(5, 3)
print(S1.area())
print(R1.area())"""



"""class Employee:
    def __init__(self, fname = None, lname = None, number = None):
        self.first_name = fname
        self.last_name = lname
        self.phone_number = number


class Supervisor(Employee):
    def __init__(self, fname=None, lname=None, number=None):
        super().__init__(fname, lname, number)
    def show_name(self):
        print(f"{self.first_name} {self.last_name} is a supervisor")


E1 = Employee("Swarnava")
E2 = Employee("Ankit")
E3 = Supervisor("Random")
E3.show_name()"""























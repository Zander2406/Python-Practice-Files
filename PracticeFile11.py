# https://www.geeksforgeeks.org/student-management-system-in-python/

STUDENT_LIST = []


class Student:
    def __init__(self, name = None, roll_number = None, marks1 = None, marks2 = None):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
    

    def accept(self, Name, RollNo, Marks1, Marks2):
        student = Student(Name, RollNo, Marks1, Marks2)
        STUDENT_LIST.append(student)
    

    def display(self, student):
        print(f"Name: {student.name}\nRoll No.: {student.roll_number}\nMarks 1: {student.marks1}\nMarks 2: {student.marks2}")
    

    def search(self, roll_num):
        for student in STUDENT_LIST:
            if student.roll_number == roll_num:
                self.display(student)
                return
        print("Student not in list")




if __name__ == "__main__":
    Studentx = Student()
    Studentx.accept("Ankit", 1, 78, 90)
    Studentx.accept("Swarnava", 2, 78, 90)
    # Studentx.display(STUDENT_LIST[1])
    Studentx.search(2)

























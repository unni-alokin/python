#class student and its child class marks

class Student():
    def __init__(self):
        self.rollno = 0
        self.st_name = ""

    def get_data(self):
        self.rollno = input("Enter your rollnumber : ")
        self.st_name = input("Enter your Name : ")
    
    def print_data(self):
        print("hai ,your Roll number is :",self.rollno)
        print("Your Name is :",self.st_name)

class Marks(Student):
    def _init_(self):
        self.subject_1 = 0
        self.subject_2 = 0
        self.subject_3 = 0
        self.subject_4 = 0
        self.subject_5 = 0
        self.subject_6 = 0
    
    def input_data(self):
        self.get_data()
        self.subject_1 = input("Enter mark 1 : ")
        self.subject_2 = input("Enter mark 2 : ")
        self.subject_3 = input("Enter mark 3 : ")
        self.subject_4 = input("Enter mark 4 : ")
        self.subject_5 = input("Enter mark 5 : ")
        self.subject_6 = input("Enter mark 6 : ")
    
    def out_data(self):
        self.print_data()
        print("Mark 1 is :",self.subject_1)
        print("Mark 2 is :",self.subject_2)
        print("Mark 3 is :",self.subject_3)
        print("Mark 4 is :",self.subject_4)
        print("Mark 5 is :",self.subject_5)
        print("Mark 6 is :",self.subject_6)
# student1 = Student()
# student1.get_data()
# student1.print_data()
student2 = Marks()
student2.input_data()
student2.out_data()
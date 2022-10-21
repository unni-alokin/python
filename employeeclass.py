#employee class and its child salary
class Employee():
    def __init__(self):
        self.employee_id = 0
        self.employee_name = ""
        self.employee_des = ""
        self.employee_adr = ""
        self.employee_phone = 0
    
    def get_data(self):
        self.employee_id = input("Hello, enter you ID number :")
        self.employee_name = input("Enter your name here : ")
        print("Choose your designation and input the number:")
        print("1.manager 2.Bussinessanalyst")
        x = input("enter the number : ")
        if (x == '1'):
            self.employee_des = "Manager"
        else:
            self.employee_des = "Bussiness analyst"
        self.employee_adr = input("Enter your address : ")
        self.employee_phone = input("Enter your phone number : ")
    
    def put_data(self):
        # print("hello ",self.employee_name)
        print("Your id is ",self.employee_id)
        print("Your designation is",self.employee_des)
        print("Your phone number is :",self.employee_phone)
        print("Your address is :",self.employee_adr)
employee1=Employee()
employee1.get_data()
class Salary(Employee):
    def _init_(self):
        self.DA = 0
        self.HRA = 0
        self.Basicpay = 0
        self.PF = 0
        self.Totalpay = 0
    def get_basicpay(self):
        self.Basicpay = int(input("Hai please enter your basic pay"))
    
    def calculate(self):
        self.HRA = round((15/100)*self.Basicpay,2)
        self.DA = round((8/100)*self.Basicpay,2)
        self.PF = round((12/100)*self.Basicpay,2)
        self.Totalpay = self.PF + self.HRA + self.DA + self.Basicpay
    
    def display(self):
        print("Hello",self.employee_name,"your salary details are as follows :")
        print("Basic pay of Rs.",self.Basicpay)
        print("DA of Rs.",self.DA)
        print("HRA of Rs.",self.HRA)
        print("Total pay of Rs.",self.Totalpay)

employee2 = Salary()
employee2.get_basicpay()
employee2.calculate()
employee2.display()
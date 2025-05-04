class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        print("Employee's amount: $", self.pay)

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        print("Employee's bonus: $", b)
        return b
    
#creating managers class
#inheriting from employee class
#creating manager class
class Manager(Employee):
    def display(self):
        print("Manager's amount: $")
        

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        print("Manager's bonus: $")




   



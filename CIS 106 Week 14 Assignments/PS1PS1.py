class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b

empl1 = Employee("Sean", "Fernandez", 60000.00)

#objects
print(empl1.first)
print(empl1.last)
print(empl1.pay)
print(empl1.email)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))
class Employee:

    num_of_employees = 0
    raise_amount = 1.04  # class variable is identical for all instances

    def __init__(self, first, last, pay):
        self.first = first  # self.first is instance variable
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_employees += 1  # instead of this we can use self.num_of_employees, but it is much better.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # instead of self.raise_amount, we can use Employee.raise_amount because if it does not find instance variable it will look for class variable. in this way, we are flexible to


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)  # it first checks the instance variables and if it does not exist, it will look for class variables
print(emp_2.raise_amount)

print(Employee.__dict__)  # prints the name space of the class
print(emp_1.__dict__)  # prints the name space of this instance
emp_1.raise_amount = 1.05  # by doing this, the rais_amount is added to emp_1 attributes but not to the emp_2
print(emp_1.__dict__)  # prints the name space of this instance

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.pay = 50000
print(emp_1.pay)
emp_1.apply_raise()  # now it will use the instance varible not the class variable
print(emp_1.pay)

print(Employee.num_of_employees)

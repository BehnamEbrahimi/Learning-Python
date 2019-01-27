class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # by inheritance, the Developer class has all the attributes and functions of the Employer.
    raise_amt = 1.1  # by changing the attibute in a sub-class, the parent will be unaffected

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # calling the constructor of the parent
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):  # !!! Never pass a mutable data type as a default argument
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for employee in self.employees:
            print('-->', employee.fullname())


print(help(Developer))  # you can see the "Method resolution order", all the attibutes and methods
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
emp_1 = Employee('Test', 'Employee', 60000)
mgr_1 = Manager('Ben', 'Abe', 90000, [dev_1])

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)

print(mgr_1.email)
mgr_1.add_emp(emp_1)
mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager)) # True
print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False

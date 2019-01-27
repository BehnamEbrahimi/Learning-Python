# Magic methods = Dunder methods = Special mehtods
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

    def __repr__(self):  # it is called when repr(self) is run. it is used to return an unambigues version of our object ---> for developers and debugging. this is the minimum meaning if we dont have str(), it returns to this method. it should be sth that we recreate the object by it
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # it is called when str(self) is run. it is used to display our object to the end user ---> for ordinary people.
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):  # this special method is called when using "+"
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(repr(emp_1))  # equal to print(emp_1.__repr__())
print(emp_1)  # equal to print(emp_1.__str__())
print(emp_1 + emp_2)  # equal to print(Employee.__add__(emp_1, emp_2))
print(len(emp_1))
print(1 + 2)  # equal to print(int.__add__(1, 2))
print('a' + 'b')  # equal to print(str.__add__('a', 'b'))
print(len('test'))  # equal to print('test'.__len__())

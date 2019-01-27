class Employee:  # methods are functions associated with the class and attibutes are class variables

    def __init__(self, first, last, pay):  # this is the constructor. "self" is always the first argument in every method, because it is basically the instance and the method receives the instance.
        self.first = first  # it is better that the instance variables have the same name as the arguments passed to the constructor
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):  # always pass the self
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)  # The __init__ method is called. The instance is created by using class name and passing the instance variables except "self", because it is passed automatically.
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())  # equal to print(Employee.fullname(emp_1))
print(Employee.fullname(emp_1))

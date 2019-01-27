class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # with this decorator, we can write a class method which does not take instance and instead takes class
    def set_raise_amt(cls, amount):  # we cannot use the word class, by convention we use cls
        cls.raise_amt = amount

    @classmethod  # class method as alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # calls the main constructor (__init__ method)

    @staticmethod # with this decorator, we can create a static method. static methods dont take anything (self or cls) as the first argument. techniaclly they are methods logically related to our class.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)  # class method can be accessed through class name and we dont have to pass in the class to the method. There is no difference if we run the class method on instance but not recommended: emp_1.ser_raise_amt(1.05).

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date)) # to run a static method, we should access it by class name

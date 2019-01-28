# sorting objects


class Employee:

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __repr__(self):  # always pass the self
        return 'Employee({}, {}, {})'.format(self.name, self.age, self.pay)


emp_1 = Employee('Corey', 50, 50000)
emp_2 = Employee('Ben', 33, 60000)
emp_3 = Employee('Jane', 23, 40000)

emloyees = [emp_1, emp_2, emp_3]


def e_sort(emp):
    return emp.age

# first way
s_employees = sorted(emloyees, key=e_sort, reverse=True)  # for comparing we have to define a function to pass to the key
print(s_employees)

# second way
s_employees = sorted(emloyees, key=lambda e: e.age)  # for such a short function we can use anonymous lambda function which is lambda arguments : expression
print(s_employees)

# third way
from operator import attrgetter
s_employees = sorted(emloyees, key=attrgetter('age'))  # for such a short function we can use anonymous lambda function which is lambda arguments : expression
print(s_employees)

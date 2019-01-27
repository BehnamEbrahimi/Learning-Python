class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # by this decorator, we define a function but we access it without "()".
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property  # we cannot assign: emp_1.fullname = "Ben Abe". for this purpose, we should use setter decorator
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # as the name suggests, this function is run whenever we want to assign sth to fullname
    def fullname(self, name):  # it must be the same name as the property
        self.first, self.last = name.split()

    @fullname.deleter  # as the name suggests, this function is run whenever we want to del(self.fullname)
    def fullname(self):
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'Ben'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Ben Abe"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del(emp_1.fullname)
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

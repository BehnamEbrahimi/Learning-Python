import logging

logger = logging.getLogger(__name__)  # get a new logger. the parameter by convention is the variable __name__ (directly: __main__, indirectly: name of the module)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')  # if you want the logger to write into a file, you must use a FileHandler
file_handler.setFormatter(formatter)  # specify format to the file_handler

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s') # not needed anymore


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')

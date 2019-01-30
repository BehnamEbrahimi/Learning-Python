import unittest
from employee import Employee
from unittest.mock import patch  # we want to mock the inforamation from the website because we dont care that the website is up or not. we can use patch as a decorator or as a context manager


class TestEmployee(unittest.TestCase):

    @classmethod  # this setUp class method will be run before all tests. for example populating a database
    def setUpClass(cls):
        print('setupClass')

    @classmethod  # this tearDown class method will be run after all tests.
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):  # to keep the code DRY. this setUp method will be run before each single test. dont forget to add self before each employee to make them instance variable
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):  # this tearDown method will be run after each single test: for example deleting files...
        print('tearDown\n')

    def test_email(self):  # the tests are not run in order: so keep the tests isolated from each other meaning they should not rely or affect each other
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:  # inside the patch we pass the object that we want to mock: we wanted to mock requests.get from employee module (the file that we wanted to test)
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')  # to make sure that the get method called with the correct URL
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

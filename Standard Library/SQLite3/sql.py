import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')  # this way is better for testing. creates a fresh database in memory. it is useful because we dont have to comment out create tables or inserting data.

# conn = sqlite3.connect('employee.db')  # it creates the file even it does not exist. if it exists, it just connects

c = conn.cursor()  # cursor helps us excute SQL commands

# # after creating the table, if we are working with the file, we comment the following code out, otherwise we will get error
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")  # datatypes in SQLite are: null, integer, real, text, blob
conn.commit()  # after each necessary transaction, commit to the database

c.execute("INSERT INTO employees VALUES ('Ben', 'Abe', 5000)")
conn.commit()

c.execute("SELECT * FROM employees WHERE last = 'Abe'")  # provide results that we can iterate through
print(c.fetchall())  # to iterate the results. fetchone: get the next row, if no row, returns None, fetchmany(5): returns 5 rows as a list, fetchall: returns a list with all results

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Jenn', 'Doe', 70000)

# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))  # Danger: injection to the database. instead use the proper way below
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})  # propper way 1
# conn.commit()

# c.execute(f"INSERT INTO employees VALUES ('{emp_3.first}', '{emp_3.last}', '{emp_3.pay}')")  # propoer way 2
# conn.commit()


def insert_emp(emp):
    with conn: # with this context manager, the transaction will automatically be commited unless there is an exception and in this case they rollback
        c.execute(f"INSERT INTO employees VALUES ('{emp.first}', '{emp.last}', '{emp.pay}')")


def get_emps_by_name(lastname): # SELECT doesnt need commit. so no context manager
    c.execute(f"SELECT * FROM employees WHERE last='{lastname}'")
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(f"""UPDATE employees SET pay = '{pay}'
                    WHERE first ='{emp.first}'  AND last ='{emp.last}' """)


def remove_emp(emp):
    with conn:
        c.execute(f"DELETE from employees WHERE first ='{emp.first}'  AND last ='{emp.last}'")


insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()

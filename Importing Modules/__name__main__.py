# when Python runs a file it give a value to the __name__ variable
print(__name__) # it returns __main__ if run directly but if it is imported it will be equal to the name of the file (first_module.py)

if __name__ == '__main__': # is this file directly run by Python?
    print("directly")
else:
    print("imported")

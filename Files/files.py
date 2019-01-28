import os

# # The Basics:
# f = open("test.txt", "r")  # to read. if the file is in another directory, you should pass the path
# f = open("test.txt", "w")  # to write
# f = open("test.txt", "a")  # to append
# f = open("test.txt", "r+")  # to read and write
# print(f.name)  # returns the file name
# print(f.mode)  # returns the file mode, r+ here
# f.close()  # if we dont use a context manager, we have to close the file, otherwise we will have leaks

# Reading Files:
# with open("test1.txt", "r") as f:  # it allows to work with the file inside the block. best practice

# # Small Files:
# f_contents = f.read() # all the contents will be loaded to memory
# print(f_contents)

# #Big Files:
# f_contents = f.readlines() # it returns a list, each value is a line in the file
# print(f_contents)

# # With the extra lines:
# f_contents = f.readline() # it returns the next line
# print(f_contents, end='') # print adds a new line
# f_contents = f.readline()
# print(f_contents)

# #Iterating through the file:
# for line in f: # reads each line, iterable
#     print(line, end = '')

# #Going Back....:
# f_contents = f.read()
# print(f_contents, end = '')

# # Printing by characters:
# f_contents = f.read(10)  # it reads the first 10 characters
# print(f_contents, end='')
# f_contents = f.read(100)
# print(f_contents, end='')
# f_contents = f.read(100) # if it already reached the end of the file, it returns empty string
# print(f_contents, end='')

# # Iterating through small chunks:
# size_to_read = 10
# f_contents = f.read(size_to_read)
# while len(f_contents) > 0:  # the length of an empty string is 0
#     print(f_contents, end='')
#     f_contents = f.read(size_to_read)

# # Iterating through small chunks, with 10 characters:
# size_to_read = 10
# f_contents = f.read(size_to_read)
# print(f.tell()) # returns the current position which is 10 here
# print(f_contents, end='')

# f.seek(0) # we can manipulate the current position by seek method. seek(0) will return the reader to the begining of the file

# f_contents = f.read(size_to_read)
# print(f_contents, end='')

# # Writing Files:
# # The Error:
# with open("test.txt", "r") as f:
#     f.write("Test") # not writable

# # Writing Starts:
# with open("test2.txt", "w") as f: # be careful if the file exists it overwrites it. if the file does not exist, it creates the file, even if there is only a pass in the block
# f.write("Test")
# f.seek(0) # this does not delete the content.
# f.write("abc") # the content of the file will be abct

# #Copying Files:
# with open("test.txt", "r") as rf:
#     with open("test_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

# # Copying the / your image:
#     # The Error
# with open("bronx.jpg", "r") as rf: # for images we should read the file in binary mode
#     with open("bronx_copy.jpg", "w") as wf:
#         for line in rf:
#             wf.write(line)

# #Copying the image starts, without chunks:
# with open("bronx.jpg", "rb") as rf: # rb means binary read
#     with open("bronx_copy.jpg", "wb") as wf: # binary write
#         for line in rf:
#             wf.write(line)

# # Copying the image with chunks:
# with open("bronx.jpg", "rb") as rf:
#     with open("bronx_copy.jpg", "wb") as wf:
#         chunk_size = 4096  # it is byte
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)

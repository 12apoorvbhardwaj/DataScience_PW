
'''
Question  1  Ans :

In Python, the open function is used to open a file. The basic syntax of the open function is:
file_object = open(file_name, mode)
where file_name is the name of the file you want to open and mode is a string that specifies the mode in which the file is opened.
There are several modes in which you can open a file:

'r' (read-only mode): This mode opens the file for reading only. If the file does not exist, a FileNotFoundError is raised.

'w' (write mode): This mode opens the file for writing only. If the file already exists, its contents are overwritten. If the file does not exist, a new file is created.

'a' (append mode): This mode opens the file for writing, but unlike 'w', it does not overwrite the contents of the file. Instead, it appends new data to the end of the file. If the file does not exist, a new file is created.

'x' (exclusive creation mode): This mode is similar to 'w', but it opens the file for writing only if the file does not already exist. If the file exists, a FileExistsError is raised.

'b' (binary mode): This mode is used to open a binary file, such as an image or a video file. It can be combined with other modes, such as 'rb' (read-only binary mode) or 'wb' (write binary mode).

't' (text mode): This mode is used to open a text file. It can be combined with other modes, such as 'rt' (read-only text mode) or 'wt' (write text mode). This is the default mode if no mode is specified.


A more convenient way to handle file I/O is to use the with statement, which automatically closes the file after the indented block of code is executed:
with open(file_name, mode) as file_object:
    # do something with the file

'''

''' 
Question 2 Ans 
It is important to close the file after you are done with it, using the close method of the file object:
file_object.close()

'''



# Question 3 Ans :

with open("text_file.txt", "w") as file:
    file.write("I want to become a Data Scientist")
with open("text_file.txt", "r") as file:
    contents = file.read()
print(contents)



# Question 4 Ans :
read()
# is used to read the entire content of a file as a string 
# Example
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

readline() # is used to read a single line from a file.
# Example
file = open("file.txt", "r")
line = file.readline()
print(line)
file.close()

readlines()
# is used to read all the lines of a file and return them as a list of strings.
# Example 
file = open("file.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# Question 5 Ans :
'''
 the with statement is used when working with resources that need to be managed, such as files.
The with statement provides a convenient way to automatically manage the lifetime of a resource,
including opening and closing the resource.

When used with the open() function, the with statement makes sure that the file is automatically
closed when the block of code inside the with statement is finished executing, even if an exception
occurs. This helps to ensure that resources are properly cleaned up and prevents potential resource leaks. 
'''
with open("file.txt", "r") as file:
    content = file.read()
    print(content)


# Question 6  Ans :

#The write() function is used to write a string to a file. Here's an example:
with open("file.txt", "w") as file:
    file.write("This is the first line of text.\n")
    file.write("This is the second line of text.")
'''
the open() function is called inside the with statement with the "w" mode argument, which opens
the file for writing. The write() function is then used to write two strings to the file. Once 
the code inside the with statement is finished executing, the file is automatically closed.
'''
# writelines() function is used to write a list of strings to a file.
with open("file.txt", "w") as file:
    lines = ["This is the first line of text.\n", "This is the second line of text."]
    file.writelines(lines)

'''
the open() function is called inside the with statement with the "w" mode argument, which opens the
file for writing. A list of strings is then created, and the writelines() function is used to write
the list of strings to the file. Once the code inside the with statement is finished executing, the
file is automatically closed.
'''
# Question 1 Ans :

''' 
In Python, the Exception class is the base class for all exceptions in the standard library, and it provides a general
framework for handling errors in your code. When you create a custom exception, it is common to create a class that
inherits from the Exception class, so that it can be used in the same way as any other exception.

    By creating a custom exception that inherits from the Exception class, your exception becomes part of the Python
exception hierarchy, allowing it to be caught and handled by existing exception-handling code that is written to handle
general exceptions. This makes it easier to write reusable and maintainable code, since you can use the same exception
-handling code for different types of exceptions.

    Inheriting from the Exception class also gives your custom exception access to its properties and methods,
such as the __str__ method, which provides a string representation of the exception. This can be useful for providing
more information about the error that occurred, which can help in debugging and fixing the problem.
'''

# Question 2 Ans :

class CustomException(Exception):
    pass

def print_exception_hierarchy(exception, level=0):
    print("  " * level + str(exception.__class__.__name__))
    for sub_exception in exception.__class__.__bases__:
        print_exception_hierarchy(sub_exception, level + 1)

print_exception_hierarchy(CustomException)


# Question 3 Ans :

''' 
The ArithmeticError class is a built-in exception in Python that is raised when an error occurs during mathematical operations.
It is a subclass of the Exception class, and there are several subclasses of the ArithmeticError class that represent specific types of arithmetic errors.

ZeroDivisionError: This error is raised when you try to divide a number by zero, which is undefined in mathematics. For example:

>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero


OverflowError: This error is raised when the result of a mathematical operation is too large to be represented as a Python int. For example:

>>> 2**1000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: int too large to convert to float

'''
# Question 4 Ans :

''' 
The LookupError class is a built-in exception in Python that is raised when an error occurs during a lookup operation, such as trying to access an element in a dictionary or list that doesn't exist.

KeyError: This error is raised when you try to access a key in a dictionary that doesn't exist. For example:

>>> d = {'a': 1, 'b': 2}
>>> d['c']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'


IndexError: This error is raised when you try to access an index in a list or array that doesn't exist.
>>> a = [1, 2, 3]
>>> a[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

'''
# Question 5 Ans :

''' 
ImportError is a built-in exception in Python that is raised when an import statement fails to find the specified module.
This can happen if the module is not installed or if the import statement has a typo or is in the incorrect format.

>>> import non_existent_module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'non_existent_module'


ModuleNotFoundError is a subclass of ImportError that was introduced in Python 3.6. It is raised specifically when
a module cannot be found, as opposed to other reasons why an import statement might fail (such as syntax errors in the import statement).

>>> import missing_module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'missing_module'


In both cases, the ImportError and ModuleNotFoundError exceptions can be caught using try-except blocks in your code, allowing you
to handle them appropriately and continue executing your program even if an error occurs. 

try:
    import missing_module
except ImportError as e:
    print("Error: Module not found.")


'''

# Question 6 Ans :

''' 
Use try and except blocks to catch exceptions: Always wrap your code in a try block and catch exceptions using an except block. This allows you to handle exceptions in a controlled and appropriate manner, rather than letting your program crash.

Be specific in catching exceptions: Try to catch specific exceptions rather than just using a generic Exception catch-all. This allows you to handle different exceptions differently and write more robust and maintainable code.

Avoid catching too broad exceptions: Catching too broad exceptions like Exception or BaseException can hide programming errors and make it harder to diagnose problems. It is better to catch only the exceptions that you know how to handle and let the others propagate up the call stack.

Raise meaningful exceptions: When raising an exception, make sure that the exception message is clear and informative. Custom exceptions should be derived from Exception and should have a meaningful message that can help diagnose the error.

Use finally blocks: Use the finally block to ensure that resources are cleaned up, even if an exception occurs. This is particularly important when working with files, database connections, or other resources that need to be closed.

Don't ignore exceptions: Don't ignore exceptions by simply catching them and doing nothing. If you catch an exception, it's important to handle it in a meaningful way, either by logging the error, re-raising it, or providing a fallback behavior.

Document exceptions: When writing code, make sure to document which exceptions might be raised by your functions and how to handle them. This makes it easier for other developers to use your code and makes your code more maintainable.

'''
# Question 1 Ans :

'''
An exception in Python is an event that occurs during the execution of a program that disrupts the normal flow
of the program's instructions. Exceptions are used to handle errors and other exceptional events in a program.
When an exception occurs, it generates an exception object that contains information about the error. The program
can catch the exception and handle it in an appropriate way.

    For example, if you try to divide a number by zero in your program, a ZeroDivisionError exception is raised.
You can catch this exception using a try-except block and display a message to the user indicating that a
division by zero is not allowed. Here is an example:
'''
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")

'''
While A syntax error occurs when a program is written in a way that is not compliant with the rules of the programming
language, such as incorrect spelling or use of a reserved keyword in an incorrect way. Syntax errors are detected by 
the interpreter when the program is being parsed, and the interpreter will halt execution and display an error message
indicating the source and nature of the error.
'''

# Question  2  Ans :

''' 
If an exception is not handled, the Python interpreter will automatically terminate the program and display a traceback
of the error, including information about the location of the error in the code, the type of exception that was raised,
and a message describing the exception. This traceback information is useful for debugging the program and determining
the cause of the exception.
Example 
'''

x = 10
y = 0
z = x / y
print(z)
'''
In this code, an attempt is made to divide x by y, which is equal to zero. This will raise a ZeroDivisionError exception,
since division by zero is undefined. If the exception is not handled, the program will terminate and display the following traceback:
Traceback (most recent call last):
  File "example.py", line 3, in <module>
    z = x / y
ZeroDivisionError: # division by zero

This traceback information shows that the error occurred in the file example.py on line 3, when the division of x by y was attempted.
The type of exception that was raised is a ZeroDivisionError, and the message associated with the exception is "division by zero".
'''

# Question 3 Ans :

''' 
In Python, the try and except statements are used to catch and handle exceptions. The basic syntax for using these statements is as follows:

try:
    # code that might raise an exception
except ExceptionType as e:
    # code to handle the exception
'''
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
except ValueError as e:
    print("Error: Invalid input.")
finally:
    print("Exiting the program.")


# Question  4 Ans :

# Given an example below 
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        raise
    else:
        print("The division was successful.")
        return result
    finally:
        print("This code will run no matter what.")

try:
    print(divide(10, 2))
except:
    print("An error occurred.")

'''
In this example, the divide function takes two arguments, a and b, and tries to perform the division a / b. If the division cannot be performed
due to a ZeroDivisionError (for example, if b is zero), the code inside the except block is executed and an error message is printed. Additionally,
the raise statement re-raises the exception so that it can be caught by the outer try block.

The else block is executed if there were no exceptions raised in the try block, and it prints a success message.

The finally block is executed regardless of whether an exception was raised or not, and it always prints the message
 "This code will run no matter what.".

Finally, the outer try block catches the exception raised in the divide function (if it was raised), and prints a generic error message.
'''

# Question 5 Ans:

''' 
Custom exceptions, also known as user-defined exceptions, are exceptions that you create yourself in your code to handle specific error conditions
that are not covered by the built-in exceptions in a programming language. Custom exceptions are used to make your code more readable, maintainable,
and easy to debug, by allowing you to raise exceptions with specific error messages that are meaningful to your code.

For example, let's say you have a program that processes bank transactions, and you want to raise an exception if a transaction amount is negative.
Here's how you could define a custom exception in Python:
'''
class NegativeAmountException(Exception):
    pass

def process_transaction(amount):
    if amount < 0:
        raise NegativeAmountException("Transaction amount cannot be negative.")
    # rest of the code to process the transaction

try:
    process_transaction(-100)
except NegativeAmountException as e:
    print(e)


'''
In this example, we define a custom exception NegativeAmountException that inherits from the built-in Exception class. In the process_transaction
function, we check if the amount is negative, and if it is, we raise our custom exception with a specific error message. Finally, in the outer try
block, we catch the NegativeAmountException and print the error message:
'''

# Question 6  Ans :


class InvalidInputException(Exception):
    pass

def calculate_factorial(n):
    if n < 0:
        raise InvalidInputException("Input number cannot be negative.")
    if n == 0:
        return 1
    return n * calculate_factorial(n-1)

try:
    print(calculate_factorial(-5))
except InvalidInputException as e:
    print(e)

''' 
In this example, we define a custom exception InvalidInputException and use it in the calculate_factorial function. If the input number n is negative,
the function raises the custom exception with a specific error message. The outer try block catches the InvalidInputException and prints the error message:
'''
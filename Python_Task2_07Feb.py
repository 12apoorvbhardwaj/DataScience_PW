# Question 1 Password Generator 
def check_password(password):
    if len(password) != 10:
        return "Invalid Password"
    if sum(map(password.count, "abcdefghijklmnopqrstuvwxyz")) < 2 or sum(map(password.count, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")) < 2:
        return "Invalid Password"
    if not any(char.isdigit() for char in password) or not any(char in "!@#$%^&*()_+,-./:;<=>?@[\]^_`{|}~" for char in password):
        return "Invalid Password"
    return "Valid Password"

# Question 2 

# Check if string starts with a particular letter
strings = ["Hello", "Hi", "Goodbye", "Hola"]
letter = "H"
result = list(map(lambda string: string.startswith(letter), strings))
print(result)


# Check if string is numeric
is_numeric = lambda x: x.isdigit()


# Sort a list of tuples having fruit names and their quantity.
fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print("Sorted fruits list:", sorted_fruits)


# Find Squares of numbers from 1 to 10
square = lambda x: x**2
result = list(map(square, range(1, 11)))
print(result)


# Find Cube of numbers from 1 to 10
cube = lambda y: y**3
result = list(map(cube, range(1, 11)))
print(result)
def is_even(num):
    return num % 2 == 0


# Check if a given number is even
num = int(input("Enter a number: "))
if is_even(num):
    print(num, "is even.")
else:
    print(num, "is odd.")

# Filer out the odd numbers in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)

#Sort a list of integers into positive and negative integers lists.
numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]
positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

positive_numbers.sort()
negative_numbers.sort(reverse=True)

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)



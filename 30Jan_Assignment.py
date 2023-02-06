# Question 1 

marks = int(input())
if marks > 90:
    grade =  "A"
elif marks > 80 and marks <= 90:
    grade = "B"
elif  marks >=60 and marks <=80:
    grade = "C"
else:
    grade = "D"
    
print(grade)

# Question 2

price = int(input())
if price > 100000 :
    tax = 0.15 * price
elif price  > 50000 and price <= 100000:
    tax = 0.1 * price
else:
    tax = 0.05 * price
print("Tax to be paid is" , tax)



# Question 3

city = input()
if city == "Delhi":
    print("Red Fort")
if city == "Agra":
    print("Taj Mahal")
if city == "Jaipur":
    print("Jal Mahal")


# Question 4

number = int(input("Enter a number: "))
count = 0
while number > 10:
    number /= 3
    count += 1
print("No of times is ",count)


# Question 5

# while loop in Python is used to execute a set of statements repeatedly until a specific condition is met.
# initialize variables
i = 1
sum = 0

# execute loop until i is less than or equal to 10
while i <= 10:
    sum = sum + i
    i = i + 1

# print the sum after loop execution
print("The sum of first 10 natural numbers is", sum)

# Question 6

# 3 different patterns : 

# Left Triangle
rows = 5

# loop to print the pattern
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end="")
    print("")


# inverted Triangle
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print("*", end="")
    print("")



# Right Triangle
for i in range(1, rows+1):
    for j in range(rows, i, -1):
        print(" ", end="")
    for k in range(1, i+1):
        print("*", end="")
    print("")


# Question 7

number = 10
while number > 0:
    print(number)
    number -= 1

# Question 8

number = 10
while number > 0:
    print(number)
    number -= 1


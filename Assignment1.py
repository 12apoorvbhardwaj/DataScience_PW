#Question 1 Solution
player = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
player.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(player)

#Question 2 Solution
li = [1,2,3,4,5,6,7,8,9,10]
sq = list(map(lambda x: x*2, li))
print(sq)

#Question 3 Solution
my_List = [1,2,3,4,5,6,7,8,9,10]
sq = list(map(lambda x: str(x), my_List))
print(sq)

#Question 4 Solution
from functools import reduce
z = [i for i in range(1, 26)]
product = reduce(lambda x, y: x*y, z)
print(product)

#Question 5 Solution
abc=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
divisible = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, abc))
print(divisible)

#Question 6 Solution
my_string=['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x: x == x[::-1], my_string))
print(palindromes)



# Question  1 Ans :
''' 
The variable list_ is a Python list, which can contain elements of different data types such as integers, strings, etc.
In this case, the elements of the list_ are strings. The variable array_list is a NumPy array, which can also contain
elements of different data types, but all the elements must have the same data type. In this case, since all the elements
of the list_ are strings, the data type of array_list will be a string.
'''
list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)

print(type(list_))      # Output: <class 'list'>
print(type(array_list)) # Output: <class 'numpy.ndarray'>


# Question  2 Ans :

''' 
    To print the data type of each and every element of both the variables list_ and array_list, you can use a for loop along
with the type() function as follows:

The first for loop iterates over each element in list_, and prints the data type of each element using the type() function.
The second for loop iterates over each element in array_list, and prints the data type of each element using the type() function.
Note that since all the elements in both list_ and array_list are strings, the data type of each element will be <class 'str'>.
Therefore, the output of both for loops will be:
'''
import numpy as np

list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_)

# Print data type of each element in list_
for elem in list_:
    print(type(elem))

# Print data type of each element in array_list
for elem in array_list:
    print(type(elem))


# Question  3 Ans :

''' 
    There will be a difference in the data type of the elements present in both the variables list_ and array_list if we create the
array_list with the data type of int.

    When we create the array_list using the dtype=int parameter, all the elements of the list_ will be converted to integers before
creating the array. Therefore, the data type of the elements in array_list will be int.

To print the data type of each and every element present in both the variables list_ and array_list, you can use a for loop along with
the type() function as follows:

The first for loop iterates over each element in list_, and prints the data type of each element using the type() function. Since all
the elements in list_ are strings, the data type of each element will be <class 'str'>.

The second for loop iterates over each element in array_list, and prints the data type of each element using the type() function.
Since all the elements in array_list are integers, the data type of each element will be <class 'numpy.int64'>.
'''
import numpy as np

list_ = [ '1' , '2' , '3' , '4' , '5' ]
array_list = np.array(object = list_, dtype = int)
for elem in list_:
    print(type(elem))

for elem in array_list:
    print(type(elem))

# Question  4 Ans :

''' 
shape attribute:

    The shape attribute is used to get the dimensions of a NumPy array. It returns a tuple of integers representing the size of the array
in each dimension. For example, if we have a two-dimensional array with 3 rows and 4 columns, the shape of the array would be (3, 4).

size attribute:

    The size attribute is used to get the total number of elements in a NumPy array. It returns a single integer value that represents
the size of the array.
'''

import numpy as np
num_array = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape of the array:", num_array.shape)
print("Size of the array:", num_array.size)

# Question  5 Ans :

import numpy as np

zeros_array = np.zeros((3, 3))
print(zeros_array)


# Question  6 Ans :

import numpy as np

identity_matrix = np.identity(5)
print(identity_matrix)


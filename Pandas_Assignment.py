# Question 1  Ans :

import pandas as pd

data = [4, 8, 15, 16, 23, 42]
d = pd.Series(data)

print(d)


# Question 2  Ans :

import pandas as pd
x = [1,2,3,4,5,6,7,8,9,10]
z = pd.Series(x)
print(z)

# Question 3  Ans :

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
my_dataframe = pd.DataFrame(data)
print(my_dataframe)


# Question 4  Ans :
'''
    In Pandas, a DataFrame is a two-dimensional labeled data structure that consists of rows and columns, similar to a spreadsheet
or a SQL table. It is one of the most important data structures in Pandas and can be thought of as a collection of Pandas Series 
that share the same index.

    On the other hand, a Series is a one-dimensional labeled data structure that holds an array of values with an associated index.
A Series is similar to a column in a spreadsheet or a column in a SQL table. The main differences between a Pandas Series and a
Pandas DataFrame are:

Dimensions: A Series is a one-dimensional array of data while a DataFrame is a two-dimensional array of data.

Data structure: A Series can contain only a single column or a single row of data with an associated index, while a DataFrame is
a collection of one or more Series, arranged in columns.

Indexing: Both a Series and a DataFrame have an index, but in a Series the index refers to the values along a single axis, while
in a DataFrame the index refers to the values along both the rows and columns.

Operations: Series and DataFrame support different operations. For example, you can perform arithmetic operations on two Series
objects, but not on two DataFrame objects directly. You can also join, merge, and pivot a DataFrame but these operations are not
possible with Series.
Consider the following data about three students:

Name	Age	Gender
Alice	25	F
Bob	30	M
Claire	27	F
To represent this data in Pandas, we can use a DataFrame. Here's how to create a Pandas DataFrame for this data:
'''
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['F', 'M', 'F']
}

df = pd.DataFrame(data)


grades = pd.Series(['A', 'B', 'B+'])
df['Grade'] = grades


# Question 5  Ans :
'''

    Pandas provides a wide range of functions that can be used to manipulate data in a DataFrame. 
Some of the commonly used functions include:

head() and tail(): These functions are used to display the first few rows or the last few rows of a DataFrame.
They are useful for quickly checking the contents of a DataFrame.

info(): This function displays a summary of the DataFrame, including the data types of each column, the number
of non-null values in each column, and the memory usage of the DataFrame. It is useful for quickly checking the
structure of a DataFrame.

describe(): This function provides summary statistics for each numerical column in the DataFrame, including the
count, mean, standard deviation, minimum, maximum, and quartile values. It is useful for getting an overview of
the distribution of the data.

drop(): This function is used to drop rows or columns from the DataFrame. It is useful for removing unwanted data
or for selecting a subset of the data.

groupby(): This function is used to group the rows of a DataFrame based on the values in one or more columns.
It is useful for aggregating data and performing summary statistics.

sort_values(): This function is used to sort the rows of a DataFrame based on the values in one or more columns.
It is useful for reordering the data or for selecting a subset of the data.

pivot_table(): This function is used to create a pivot table from a DataFrame, where the rows and columns are 
specified by one or more columns, and the values are calculated using an aggregation function. It is useful for
summarizing and analyzing data.

'''
#  groupby
import pandas as pd
data = {
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'Sales': [1000, 2000, 1500, 1800, 900, 2200, 1200, 1900]
}
df = pd.DataFrame(data)
sales_by_region = df.groupby('Region').sum()
print(sales_by_region)


# Question 6  Ans :
''' 
    
    Both Series and DataFrame are mutable in nature, meaning you can modify their contents by adding, deleting,
or modifying elements. On the other hand, Panel is a three-dimensional data structure that is deprecated in the
current version of Pandas and is no longer recommended for use.

'''
# Question 7  Ans :
''' 
    To create a DataFrame using multiple Series, we can use the pd.DataFrame() function and pass a dictionary of
Series as an argument. Each Series will represent a column of the DataFrame, and the keys of the dictionary will
be used as the column names. Here's an example:
'''
import pandas as pd
names = pd.Series(['Alice', 'Bob', 'Claire'])
ages = pd.Series([25, 30, 27])
genders = pd.Series(['Female', 'Male', 'Female'])
df = pd.DataFrame({'Name': names, 'Age': ages, 'Gender': genders})
print(df)

''' 
     we create three Series, one for each column of the DataFrame. We then pass a dictionary of these Series to the
pd.DataFrame() function to create the DataFrame. The keys of the dictionary ('Name', 'Age', and 'Gender') are used
as the column names of the DataFrame, and the values of the dictionary are the corresponding Series.
'''



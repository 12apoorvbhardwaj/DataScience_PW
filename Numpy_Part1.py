'''          Pandas Advance Assignment            '''
# Question 1 Ans :
'''
read_csv() - This function is used to read a CSV file and return a DataFrame object.
drop() -     This function is used to drop specified labels from rows or columns of a DataFrame.
groupby() -  This function is used to group a DataFrame by one or more columns and perform operations on the grouped data.
merge() -    This function is used to merge two or more DataFrames based on a common column.
pivot_table() -    This function is used to merge two or more DataFrames based on a common column.
'''
# read_csv
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())


# Drop Example
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 'gender': ['F', 'M', 'M', 'M']}
df = pd.DataFrame(data)
df = df.drop('gender', axis=1)
print(df.head())

# groupby  Example
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40], 'gender': ['F', 'M', 'M', 'M'],'salary': [50000, 60000, 70000, 80000]}
df = pd.DataFrame(data)
grouped = df.groupby('gender')
mean_salary = grouped['salary'].mean()
print(mean_salary)

# merge Example
data1 = {'name': ['Alice', 'Bob', 'Charlie', 'David'],'age': [25, 30, 35, 40]}
df1 = pd.DataFrame(data1)
data2 = {'name': ['Bob', 'Charlie', 'David', 'Edward'], 'salary': [60000, 70000, 80000, 90000]}
df2 = pd.DataFrame(data2)
merged = pd.merge(df1, df2, on='name')
print(merged)

# Pivot Table Example
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'], 'age': [25, 30, 35, 40, 45],'gender': ['F', 'M', 'M', 'M', 'M'],'salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(index='gender', columns='age', values='salary', aggfunc='mean')
print(pivot_table)


# Question 2 Ans :

def reindex_dataframe(df):
    new_index = pd.Index(range(1, 2*len(df), 2))
    df = df.set_index(new_index)
    return df

# Question 3 Ans :

import pandas as pd

def calculate_sum(df):
    values = df['Values'].tolist()  
    sum_of_first_three = sum(values[:3])
    print("Sum {}".format(sum_of_first_three))

# Question 4 Ans :

df = pd.DataFrame({'Text': ['This is a sentence', 'Another sentence with more words']})
df = add_word_count_column(df)
print(df)



# Question 5 Ans :

''' 
DataFrame.size:
     Returns the total number of elements in the DataFrame, which is the product of the number of rows and the number of columns.
In other words, DataFrame.size returns the total number of cells in the DataFrame, including cells that may be empty or NaN. For example:

DataFrame.shape:
     Returns a tuple that contains the number of rows and columns in the DataFrame, respectively. In other words, DataFrame.shape returns
the size of the DataFrame in terms of its dimensions.

'''
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.size) # Output: 6

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.shape)

# Question 6 Ans :
'''
    In the example above, the read_excel() function is used to read an Excel file named 'file.xlsx' and load the data from the sheet named
'Sheet1' into a Pandas DataFrame called df.
The read_excel() function has many optional parameters that you can use to customize the way the data is loaded into the DataFrame, such as
specifying the range of rows and columns to read, the data types of the columns, etc. You can refer to the Pandas documentation for more
information on the available parameters of the read_excel() function.
'''
import pandas as pd
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')


# Question 7 Ans :

import pandas as pd
def add_username_column(df):
    df['Username'] = df['Email'].str.split('@').str[0]
    return df

'''
    The add_username_column() function takes a Pandas DataFrame df as input and returns the modified DataFrame with a new 'Username' column.
The str accessor is used to apply string operations to each element of the 'Email' column. In this case, we use the split() method to split
each email address by the '@' character, and then we use the str[] indexing operator to extract the first element of the resulting list,
which is the username part.

You can call this function by passing your DataFrame df as input:

'''
# Question 8 Ans :


def select_rows(df):
    new_df = df[(df['A'] > 5) & (df['B'] < 10)]
    return new_df

# Question 9 Ans :

def calculate_statistics(df):
    mean = df['Values'].mean()
    median = df['Values'].median()
    std = df['Values'].std()
    return mean, median, std


df = pd.DataFrame({'Values': [1, 2, 3, 4, 5]})
mean, median, std = calculate_statistics(df)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std}")


# Question 10 Ans :

def add_moving_average_column(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-02-20', end='2023-02-26'), 'Sales': [10, 20, 30, 40, 50, 60, 70]})
df = add_moving_average_column(df)
print(df)


# Question 11 Ans :

def add_weekday_column(df):
    df['Weekday'] = df['Date'].dt.strftime('%A')
    return df

df = pd.DataFrame({'Date': pd.date_range(start='2023-02-20', end='2023-02-26')})
df = add_weekday_column(df)
print(df)


# Question 12 Ans :

import pandas as pd

def select_january_rows(df):
    start_date = pd.Timestamp('2023-01-01')
    end_date = pd.Timestamp('2023-01-31')
    return df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]


# Question 13 Ans :

import pandas as pd
'''
    Here, pd is an alias for pandas, which is a commonly used alias in the Pandas community. By importing pandas with
the alias pd, we can refer to Pandas functions with the shorter alias instead of typing out the full name every time.
'''

# Question 1 

'''

A database is an organized collection of data that can be easily accessed, managed, and updated. Databases can be used to store various types of information,
such as customer data, financial transactions, product inventory, and more. They are essential for the proper functioning of many applications and websites.

    There are two main types of databases: SQL and NoSQL.

    SQL (Structured Query Language) databases are relational databases that are based on a predefined schema, which defines the structure of the data and the
relationships between different tables. They are widely used and well-established in the industry, and are suitable for applications that require complex queries
and transactions. Some popular SQL databases include MySQL, Oracle, and PostgreSQL.

    NoSQL (Not Only SQL) databases, on the other hand, do not rely on a predefined schema. Instead, they are designed to handle unstructured or semi-structured
data, such as JSON, XML, or key-value pairs. They are highly scalable and flexible, making them ideal for applications that need to handle large volumes of data,
such as social media platforms, e-commerce sites, and IoT devices. Some popular NoSQL databases include MongoDB, Cassandra, and Amazon DynamoDB.

'''
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Question 2 Ans :

''' 
    DDL stands for Data Definition Language, which is a set of SQL commands used to define and manage the structure of a database. DDL commands are used to create,
modify, and delete database objects, such as tables, indexes, and views.

* CREATE:
     This command is used to create a new database object, such as a table, index, or view. Here's an example of creating a table in SQL:

CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
);

* DROP:
     This command is used to delete a database object. For example, to delete the "customers" table that we created earlier, we can use the following command:
DROP TABLE customers;

* ALTER :
    This command is used to modify the structure of an existing database object. For example, we can use the ALTER command to add a new column to the "customers"
table that we created earlier:

ALTER TABLE customers ADD COLUMN phone VARCHAR(20);

* TRUNCATE:
     This command is used to delete all data from a table while keeping the table structure intact. For example, to delete all the data from the "customers" table
without deleting the table structure itself, we can use the following command:

TRUNCATE TABLE customers;

'''
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Question 3 Ans :

'''
    DML stands for Data Manipulation Language, which is a set of SQL commands used to manage and manipulate the data stored in a database. DML commands are used to insert,
update, and delete data in a database.Here is a brief explanation of some commonly used DML commands and their purposes, along with an example:

INSERT:
     This command is used to insert new data into a table. Here's an example of inserting a new row into the "customers" table:
INSERT INTO customers (id, name, email, phone)

VALUES (1, 'John Smith', 'john.smith@example.com', '555-1234');

UPDATE:
    This command is used to modify existing data in a table. For example, to update the email address of a customer with the ID 1 in the "customers" table,
we can use the following command:

UPDATE customers SET email = 'john.smith@gmail.com' WHERE id = 1;

DELETE:
     This command is used to delete data from a table. For example, to delete a customer with the ID 1 from the "customers" table, we can use the following command:
DELETE FROM customers WHERE id = 1;
'''

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Question 4 Ans :

''' 
    DQL stands for Data Query Language, which is a set of SQL commands used to retrieve data from a database. DQL commands are used to query the data in a database and return the results.
Here is an explanation of the commonly used DQL command SELECT, along with an example:
SELECT:
     This command is used to retrieve data from one or more tables in a database. It allows you to specify the columns you want to retrieve, the table or tables from which to retrieve the data,
and any conditions or filters that should be applied to the data. Here's an example of using the SELECT command to retrieve data from a "customers" table:

    SELECT name, email, phone FROM customers WHERE id = 1;

SELECT command to retrieve specific columns from the "customers" table, and we also used a WHERE clause to filter the results based on a specific condition.
You can use many other features of the SELECT command to retrieve data from the database, such as aggregate functions, sorting, grouping, and joining multiple tables.

''' 
'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Question 5 Ans :

''' 

    A primary key is a column or set of columns in a table that uniquely identifies each row in the table. Primary keys are used to ensure that each row in a
table is unique and to help maintain data integrity. A primary key is defined when a table is created and cannot be null. Common examples of primary keys are
an ID number or a social security number. A foreign key is a column or set of columns in one table that refers to the primary key of another table. A foreign
key establishes a relationship between two tables, where one table (the "child" table) references another table (the "parent" table). Foreign keys are used to
ensure data consistency and to enforce referential integrity.

    Here is an example of how primary and foreign keys can be used in a database. Let's say we have two tables: "orders" and "customers". The "orders" table
contains information about orders, such as the order ID, the customer ID, and the order date. The "customers" table contains information about customers, such
as the customer ID, name, and address.

    In this scenario, the "customer ID" column in the "orders" table would be a foreign key that references the primary key in the "customers" table. This means
that each order in the "orders" table must have a valid customer ID that exists in the "customers" table. This ensures that there are no orphaned records in the
"orders" table and that each order is associated with a valid customer.

    In summary, a primary key is a column or set of columns in a table that uniquely identifies each row in the table, while a foreign key is a column or set of
columns in one table that refers to the primary key of another table. Together, primary and foreign keys help establish relationships between tables and ensure
data consistency and referential integrity in a database.

'''

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Question 6 Ans :


import mysql.connector

# Establishing a connection to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Creating a cursor object to interact with the database
mycursor = mydb.cursor()

# Executing an SQL query using the execute() method
mycursor.execute("SELECT * FROM customers")

# Fetching the results of the query using the fetchall() method
result = mycursor.fetchall()

# Printing the results
for row in result:
  print(row)

#   cursor.execute ():
    # This method helps us to execute the query and return records according to the query. The syntax of the execute () function is:
execute (query, args = None)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Question 7 Ans:

''' 
In a typical SQL query, the clauses are executed in the following order:

FROM: 
     This clause is executed first, and it specifies the table or tables that the query will retrieve data from.

WHERE:
     This clause is executed second, and it specifies the conditions that the data retrieved by the query must satisfy.
The WHERE clause filters the data to be retrieved based on a specified condition.

GROUP BY:
     This clause is executed third, and it groups the retrieved data based on one or more columns.
This is useful when you want to perform aggregate functions such as SUM, AVG, COUNT, and MAX on the data.

HAVING:
     This clause is executed fourth, and it is used in conjunction with the GROUP BY clause to specify conditions 
that the groups of data must satisfy. This is similar to the WHERE clause, but it operates on groups of data rather than individual rows.

SELECT:
     This clause is executed fifth, and it specifies the columns that should be retrieved from the table or tables specified
in the FROM clause.

ORDER BY:
     This clause is executed sixth, and it specifies the order in which the retrieved data should be sorted.
The sorting can be done in ascending or descending order.

LIMIT:
     This clause is executed last, and it limits the number of rows that are returned by the query.

It's important to note that not all clauses are required in every SQL query. The clauses that are required depend on the
specific query being executed. Also, some clauses like GROUP BY, HAVING, and ORDER BY may be omitted in simple queries.
'''
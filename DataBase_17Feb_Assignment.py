# Question 1 Ans :
''' 

    MongoDB is a popular open-source, document-oriented NoSQL database that stores data in JSON-like documents. It is designed
to be highly scalable, flexible, and easy to work with. Non-relational databases, also known as NoSQL databases, are databases
that do not use a traditional tabular structure to store data. Instead, they use a variety of data models, such as key-value,
document-oriented, graph, or column-family, to store data.

There are several scenarios where MongoDB is preferred over SQL databases:

Unstructured or semi-structured data:
    If your data is unstructured or semi-structured, it may be easier to work with a document-oriented database like MongoDB,
which can store data in a more flexible, JSON-like format.

Large volumes of data:
    MongoDB is designed to be highly scalable, and can handle large volumes of data with ease.

High availability:
    MongoDB provides automatic sharding and replication, which ensures high availability and reliability of your data.

Agile development:
    With MongoDB, you can quickly and easily add new fields to your documents, making it easier to iterate on your data model
and adapt to changing requirements.

Real-time analytics:
    MongoDB supports real-time analytics and ad-hoc querying, making it easier to perform complex queries on your data.

Overall, MongoDB is a good choice when you need to store and manage large volumes of unstructured or semi-structured data,
and when you need a highly scalable, flexible, and agile database solution.

'''

'''------------------------------------------------------------------------------------------------------------------------'''
# Question 2 Ans :
''' 
    MongoDB is a NoSQL document-oriented database that is designed to be highly scalable, flexible, and easy to work with.
Here are some of the key features of MongoDB:

Document-oriented:
     MongoDB stores data in flexible, JSON-like documents that can have varying structures, making it easy to work with
unstructured or semi-structured data.

Scalability:
     MongoDB is designed to be highly scalable, with support for automatic sharding and horizontal scaling, allowing it
to handle large volumes of data.

Indexing:
     MongoDB provides a variety of indexing options, including single-field, compound, text, and geospatial indexes, to
help you optimize your queries.

Aggregation:
     MongoDB supports a powerful aggregation framework that allows you to perform complex data analysis and aggregation
tasks, such as grouping, filtering, and sorting.

Replication and High Availability:
     MongoDB provides automatic replication and failover, ensuring that your data is always available and protected 
against hardware or network failures.

Flexible data model:
     MongoDB's flexible data model allows you to add new fields to documents as your requirements change, making it
easy to adapt to evolving data models.

ACID Transactions:
     MongoDB supports ACID transactions, allowing you to maintain data consistency and integrity across multiple operations.

Rich query language:
     MongoDB provides a rich query language that supports complex queries, including join operations, nested queries, and geospatial queries.

Overall, MongoDB is a powerful and flexible NoSQL database that provides a wide range of features to help you store, manage, and analyze large volumes of data. Its document-oriented model, scalability, indexing, and aggregation capabilities, high availability, flexible data model, ACID transactions, and rich query language make it an attractive option for many different types of applications.
'''

'''------------------------------------------------------------------------------------------------------------------------'''
# Question 3 Ans :

import pymongo
# Connect to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')
# Create a new database
db = client['mydatabase']
# Create a new collection in the database
collection = db['mycollection']

'''------------------------------------------------------------------------------------------------------------------------'''
# Question 4 Ans :

import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Get a reference to the "mydatabase" database
db = client['mydatabase']

# Get a reference to the "mycollection" collection
collection = db['mycollection']

# Insert one record
record = {'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}
insert_result = collection.insert_one(record)
print('Inserted record ID:', insert_result.inserted_id)

# Insert multiple records
records = [
    {'name': 'Jane Smith', 'age': 25, 'email': 'janesmith@example.com'},
    {'name': 'Bob Johnson', 'age': 40, 'email': 'bobjohnson@example.com'}
]
insert_result = collection.insert_many(records)
print('Inserted record IDs:', insert_result.inserted_ids)

# Find one record
result = collection.find_one({'name': 'John Doe'})
print('Found one record:', result)

# Find all records
results = collection.find()
print('Found all records:')
for result in results:
    print(result)


'''------------------------------------------------------------------------------------------------------------------------'''
# Question 5 Ans :

import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Get a reference to the "mydatabase" database
db = client['mydatabase']

# Get a reference to the "mycollection" collection
collection = db['mycollection']

# Find all records in the collection
results = collection.find()
print('All records:')
for result in results:
    print(result)

# Find records that match specific criteria
results = collection.find({'age': {'$gt': 30}})
print('Records with age > 30:')
for result in results:
    print(result)


'''------------------------------------------------------------------------------------------------------------------------'''
# Question 6 Ans :

''' 
sort method () :

    In MongoDB, the sort() method is used to sort the documents in a collection based on one or more fields. The sort() method
takes one parameter, which is an object that specifies the fields to sort on and the sort order for each field.
The sort order is specified using the values 1 (for ascending order) and -1 (for descending order). If multiple fields are specified,
the documents are first sorted by the first field, and then by the second field, and so on.

    Here's an example code to demonstrate how to use the sort() method to sort the documents in the mycollection collection by the
age field in descending order:
'''
results = collection.find().sort('age', -1)
print('All records, sorted by age:')
for result in results:
    print(result)


'''------------------------------------------------------------------------------------------------------------------------'''
# Question 7 Ans :

''' 
    In MongoDB, the delete_one() and delete_many() methods are used to remove documents from a collection that match a given query criteria.
The drop() method is used to completely remove a collection from a database.
Here's a brief explanation of each method:

delete_one(filter):
     Removes a single document from the collection that matches the given filter criteria. If there are multiple documents that match the
filter, only the first document will be removed.

delete_many(filter):
     Removes all documents from the collection that match the given filter criteria.

drop():
     Completely removes the collection from the database. All documents in the collection will be permanently deleted.

These methods are useful for managing the contents of a MongoDB database. delete_one() and delete_many() can be used to remove documents that
are no longer needed, while drop() can be used to completely remove a collection from the database.

    It's important to use caution when using these methods, as they can result in the permanent deletion of data. It's recommended to test any 
data removal operations on a non-production database before running them on a production database.

'''


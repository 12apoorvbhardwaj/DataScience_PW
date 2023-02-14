# Question 1  Ans :

''' 

    Multithreading in Python is a technique of creating and running multiple threads simultaneously to improve the performance of a program.
A thread is a lightweight process that runs concurrently with other threads in a program, sharing the same resources and memory space.
Multithreading is used to improve the performance of a program by utilizing the available resources of a system, especially in situations
where there are a large number of I/O-bound tasks that can benefit from parallel execution. Multithreading allows a program to perform multiple
tasks simultaneously, thereby reducing the overall execution time and improving the efficiency of the program.

    Python has a built-in module called threading that is used to handle threads in Python. The threading module provides a high-level interface
for creating and managing threads in Python. It provides several classes and functions that can be used to create and manage threads, such as Thread,
Lock, Semaphore, Event, Condition, and more. These classes and functions make it easy to create, start, stop, and manage threads in Python, and they
provide a safe and efficient way to handle concurrency in Python programs.

'''

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Question 2  Ans :

''' 

    The threading module in Python is used to create and manage threads in a Python program. It provides a high-level interface for creating and managing threads,
making it easy to implement concurrency in a program.

The threading module is used for the following purposes:

Improving performance:
    Multithreading can be used to improve the performance of a program by allowing it to perform multiple tasks simultaneously.
This can be particularly useful in situations where a program has a large number of I/O-bound tasks that can benefit from parallel execution.

Simplifying concurrency:
     The threading module provides a simple and convenient way to implement concurrency in a program. It provides several classes and functions
that make it easy to create, start, stop, and manage threads in Python. It also provides synchronization primitives, such as locks and semaphores,
which can be used to ensure that threads access shared resources safely.

Responsive user interfaces:
    Multithreading can be used to create responsive user interfaces in a program. By using threads to perform long-running tasks in the background,
a program can remain responsive to user input and provide a better user experience.

Overall, the threading module in Python is a powerful tool for handling concurrency in a program. It makes it easy to create and manage threads,
and provides synchronization primitives to ensure that threads access shared resources safely. By using multithreading, a program can improve its
performance, simplify concurrency, and create responsive user interfaces.

'''
# aliveCount() function :

''' 
activeCount() function is a method of the threading module in Python that is used to get the number of active threads in the current thread's ThreadGroup.
The activeCount() method returns the number of threads that are currently active and running in the current thread's ThreadGroup. A thread is considered
active if it has been started and has not yet finished or been stopped. The method does not count threads that are blocked or waiting for a lock or semaphore.

Here is an example of how to use the activeCount() function:
'''
import threading

def my_function():
    return 1

t1 = threading.Thread(target=my_function)
t2 = threading.Thread(target=my_function)
t3 = threading.Thread(target=my_function)


t1.start()
t2.start()
t3.start()
num_active_threads = threading.activeCount()

print("Number of active threads:", num_active_threads)

# CurrentThread() function :
'''
The currentThread() method returns the current thread object that is associated with the calling code. It returns a Thread object, which represents the thread
of execution for the current code. This method can be useful for debugging and logging purposes, as it allows you to identify the current thread that is executing the code.
'''

import threading
def my_function():
    current_thread = threading.currentThread()
    print("Current thread name:", current_thread.name)

t = threading.Thread(target=my_function, name="MyThread")

t.start()


# enumerate() function :
'''
The enumerate() function is a built-in function in Python that allows you to iterate over a sequence (e.g. a list, tuple, or string) and keep track of the index of the current item in the sequence.

The enumerate() function takes an iterable object (e.g. a list) as its argument and returns an enumerate object, which is an iterator that produces pairs of (index, item) for each item in the iterable.
The index is the index of the current item, starting from 0, and the item is the value of the current item in the iterable.
'''
my_list = ["apple", "banana", "cherry"]

for i, item in enumerate(my_list):
    print(i, item)


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# Question 3  Ans :

# run() function :

'''
run() function :  is the entry point for a thread, and it's the function that's executed when the start() method is called on the thread.
It contains the code that will be run in the thread. If you subclass the Thread class and override the run() method, you can define the behavior of the thread.
'''
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Starting thread ", self.name)
        # do some work here
        print("Exiting thread ", self.name)

t = MyThread()
t.start()

# start() function 

''' 
    The start() function starts a new thread and calls the run() method of the thread. When you call start(), the new thread is created and then it calls the run() function.
The start() function returns immediately, and the new thread starts executing in the background.
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()  # start the new thread

# join()  Function

'''
The join() function waits for a thread to complete. It blocks the calling thread until the thread it's waiting for has finished executing.
When the thread finishes, the join() function returns.
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()  # start the new thread
t.join()   # wait for the thread to finish
print("Thread finished")

# isAlive() Function 
''' 
The isAlive() function checks whether a thread is still running or has finished executing.
It returns True if the thread is still running and False if it has finished.
'''

import threading
import time

def my_thread():
    time.sleep(2)

t = threading.Thread(target=my_thread)
t.start()

while t.isAlive():
    print("Thread is still running")
    time.sleep(1)

print("Thread has finished")


'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# Question 4  Ans :

import threading
def print_squares():
    for i in range(10):
        print(f"{i} squared is {i**2}")

def print_cubes():
    for i in range(10):
        print(f"{i} cubed is {i**3}")

thread1 = threading.Thread(target=print_squares)
thread2 = threading.Thread(target=print_cubes)
thread1.start()
thread2.start()

thread1.join()
thread2.join()

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# Question 5  Ans :

# Advantages :

'''
Increased performance:
     Multithreading can improve the performance of applications by allowing multiple threads to execute in parallel
and thus utilize the available CPU resources more efficiently. This can lead to faster  response times and increased throughput.

Responsiveness:
     Multithreading can help keep the application responsive by allowing time-consuming tasks to be executed in the background while
the main thread handles user interaction.

Resource sharing:
    Multithreading enables efficient resource sharing by allowing multiple threads to access shared data structures and resources without the need for complex synchronization mechanisms.

Modular design:
    Multithreading enables a modular design of applications by allowing different tasks to be executed in separate threads, which can simplify the code and make it easier to maintain.
'''
# Disadvantages :

''' 
Complexity:
    Multithreaded programming can be more complex than single-threaded programming, requiring careful design and synchronization to avoid problems such as race conditions, deadlocks, and thread starvation.

Overhead:
     Multithreading can introduce additional overhead due to the need for context switching between threads, which can impact performance.

Debugging:
     Debugging multithreaded applications can be more difficult than debugging single-threaded applications, as it can be challenging to reproduce and diagnose problems that arise from thread interactions.

Resource contention:
     Multithreading can lead to resource contention and contention can lead to locking and synchronization overheads.
'''

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# Question 6  Ans :

''' 

Deadlock:

    A deadlock occurs when two or more threads are blocked and waiting for each other to release resources or locks that they currently hold. As a result, none of the threads can proceed,
and the application becomes stuck in a state where no progress is possible. Deadlocks can occur when multiple threads hold locks on shared resources and wait for each other to release them.

Race condition:

    A race condition occurs when the outcome of a program depends on the timing or order in which multiple threads execute. Specifically, it occurs when two or more threads access and modify
shared data at the same time, and the final result depends on the order in which the threads execute. Race conditions can lead to inconsistent and unpredictable behavior in the application.

To prevent deadlocks and race conditions, it is important to design thread-safe applications that ensure proper synchronization and avoid resource contention. Synchronization mechanisms like locks, semaphores, and monitors can be used to prevent deadlocks by ensuring that threads access shared resources in a mutually exclusive manner. To prevent race conditions, it is important to ensure that shared data is accessed and modified in a thread-safe manner using synchronization mechanisms.

'''
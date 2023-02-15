# Question 1 Ans : 

''' 
    Multiprocessing in Python is a way to use multiple CPU cores to parallelize and speed up the execution of CPU-bound tasks in Python programs.
It allows Python code to take advantage of multiple CPU cores to perform computationally intensive tasks, such as numerical simulations or data
processing, much faster than if they were executed on a single core.

    In Python, the multiprocessing module provides a way to create processes, each running in its own independent memory space, and communicate
with them using inter-process communication (IPC) mechanisms such as pipes, queues, or shared memory. The multiprocessing module provides a easy 
simple and consistent interface for parallelizing Python code.

    Multiprocessing is useful in Python because it can significantly improve the performance of CPU-bound tasks by distributing the workload across
multiple CPU cores. This is especially important in scientific computing, machine learning, data analysis, and other applications that require heavy
computation. With multiprocessing, Python programs can take advantage of the full computational power of modern CPUs and reduce the time required for
long-running tasks. Additionally, multiprocessing can be used to create responsive GUI applications and web servers that can handle multiple requests simultaneously.
'''

# Question 2 Ans : 
''' 
Multiprocessing and multithreading are both techniques used to improve the performance of programs by executing multiple tasks concurrently.
However, there are some important differences between the two approaches:
Memory sharing: 
    In multiprocessing, each process has its own memory space and does not share memory with other processes. In contrast, threads in
multithreading share memory with each other and with the parent process.

Parallelism:
     In multiprocessing, each process runs on a separate CPU core, which allows for true parallelism. In multithreading, all threads 
share a single CPU core, which can lead to concurrency (the appearance of simultaneous execution) but not true parallelism.

Overhead:
     Multiprocessing has a higher overhead than multithreading because starting a new process involves creating a new memory space and
copying the parent process's code and data. In contrast, starting a new thread involves only creating a new stack and a small amount of bookkeeping.

Communication:
     In multiprocessing, communication between processes is typically done using IPC mechanisms such as pipes, queues, or shared memory.
In multithreading, communication between threads is done using shared memory, which can lead to synchronization issues and race conditions.

Complexity:
     Multiprocessing is generally more complex than multithreading, as it involves more inter-process communication and coordination.
Multithreading is generally simpler to implement and debug, but can be prone to synchronization issues and other concurrency-related bugs.

    In summary, multiprocessing and multithreading are both useful techniques for improving program performance, but they have different
trade-offs in terms of memory sharing, parallelism, overhead, communication, and complexity. The choice between them depends on the specific
requirements of the program and the available hardware resources.

'''

# Question 3 Ans :

import multiprocessing

def worker():
    print("Worker process started")
    print("Worker process finished")

if __name__ == '__main__':
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    print("Main process finished")


# Question 4 Ans :
''' 
    A multiprocessing pool in Python is a group of worker processes that are created to execute tasks concurrently. The multiprocessing pool allows
for easy parallelization of a function across a large number of inputs, by distributing the inputs across multiple worker processes and automatically
collecting the results.

    The multiprocessing.Pool class in Python provides a simple interface for creating a pool of worker processes. You can create a pool of any size,
and use its map() method to apply a given function to a list of inputs in parallel. The map() method will automatically distribute the inputs across
the worker processes, and collect the results when they are finished.

    The multiprocessing pool is used to speed up the execution of a function that takes a lot of time to execute, by dividing the task into smaller sub-tasks
that can be executed in parallel. This technique is called parallel processing or parallel computing. By using a pool of worker processes, the function can be
executed on multiple CPU cores simultaneously, which can significantly reduce the overall execution time.
''' 
import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)

# Question 5 Ans : 

''' 
    To create a pool of worker processes in Python using the multiprocessing module, you can use the multiprocessing.Pool class.
Here's an example code that creates a pool of worker processes with 4 processes:
'''
import multiprocessing

def worker_function(x):
    """Function to be executed by worker processes"""
    result = x ** 2
    return result

if __name__ == '__main__':
    # Create a pool of 4 worker processes
    with multiprocessing.Pool(processes=4) as pool:
        # Execute the worker function on a range of inputs
        inputs = range(10)
        results = pool.map(worker_function, inputs)

    print(results)

''' 
    In this code, we define a worker_function() that will be executed by the worker processes. 
We then create a pool of 4 worker processes using the multiprocessing. Pool() constructor.
The processes argument specifies the number of worker processes to create. We then use the map()
method of the pool object to apply the worker_function() to a range of inputs. The map() method will
automatically distribute the inputs across the worker processes and collect the results. The results
are stored in the results list, which we print out at the end of the program.
Note that we use a context manager (with) to ensure that the pool is properly cleaned up when the program
is finished. This is not strictly necessary, but it is good practice to avoid leaving zombie processes
running in the background. Also note that the if __name__ == '__main__' guard is used to ensure that the
code inside it is only executed when the script is run as the main program, and not when it is imported as
a module. This is important to avoid spawning unnecessary child processes when the script is imported by other programs.

'''

# Question 6 Ans : 
import multiprocessing

def print_number(num):
    """Function to be executed in the child process"""
    print("Process {} prints {}".format(num, num))

if __name__ == '__main__':
    # Create a new process for each number
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=print_number, args=(i,))
        processes.append(p)
    
    # Start all processes
    for p in processes:
        p.start()
    
    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("Main process finished")

''' 
In this code, we define a function print_number(num) that will be executed in each child process.
This function takes an argument num and prints it to the console. 
    
    We then create 4 new processes, one for each number from 0 to 3. We use a for loop to create a
new Process object for each number, with the target argument set to print_number and the args argument
set to a tuple containing the number.
    
    We then start all processes using a for loop and the start() method. This will invoke the print_number()
function in each child process, printing the corresponding number to the console. We then wait for all child
processes to finish using another for loop and the join() method. This blocks the main process until all child
processes have completed.

Finally, we print a message indicating that the main process has finished.

'''
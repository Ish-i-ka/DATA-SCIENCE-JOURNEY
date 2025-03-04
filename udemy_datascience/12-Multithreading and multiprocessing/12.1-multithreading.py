#Multithreading is used when
#In I/O operations
#In concurrent operations.

import threading
import time

#single threading
def print_numbers():
    for i in range(10):
        time.sleep(2)
        print(f"Number:{i}")

def print_letters():
    for letter in "ishika":
        time.sleep(2)       #gives time gap for 2seconds
        print("Letter:",letter)
        
t=time.time()         #gives current time
print_numbers()
print_letters()
fin_time = time.time() - t
print(fin_time)


#multi threads so that when one function is sleeping then the other function can work.
def print_numbers():
    for i in range(10):
        time.sleep(2)
        print(f"Number:{i}")

def print_letters():
    for letter in "ishika":
        time.sleep(2)      
        print("Letter:",letter)
        
#Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t=time.time()

#Starting the threads
t1.start()
t2.start()
#Wait for threads to complete then finally join into the main single thread
t1.join()
t2.join()

fin_time = time.time() - t
print(fin_time)
   
   
#By multi threading we see that the time taken in total is lesser than single thread as multi tasking occurs in multi threading     
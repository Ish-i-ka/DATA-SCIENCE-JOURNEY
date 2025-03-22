# Scenario: Factorial calculation
# Factorial calculations for large numbers, 
# invove significant computations. Multiprocessing
# can be used to distribute the workload across multiple
# CPU cores, improving performance.

import multiprocessing
import time
import math
import sys

#Setting the max number of digits for integer conversion
sys.set_int_max_str_digits(100000)

#function to compute the factorial
def compute_factorial(n):
    print(f"Computing factorial of {n}")
    res = math.factorial(n)
    print(f"Factorial of {n} is {res}")
    return res 

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]
    t = time.time()
    
    #create a pool of worker processes
    with  multiprocessing.Pool() as pool:
        results  = pool.map(compute_factorial,numbers)
        
    fin_time = time.time() 
    print(f"Results: {results}")
    print(f"Time taken: {fin_time - t} seconds")
    
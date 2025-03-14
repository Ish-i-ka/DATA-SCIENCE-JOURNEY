#MultiThreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(2)
    return f"Number = {number}"

numbers = [0,1,2,3,4,5,6,7,8,9]

t = time.time()
with ThreadPoolExecutor(max_workers = 3) as executor:
    results = executor.map(print_numbers,numbers)
    
for result in results:
    print(result)

fin_time = time.time() - t
print(fin_time)
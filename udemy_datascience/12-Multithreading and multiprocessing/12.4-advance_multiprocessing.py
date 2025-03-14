## Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def print_num(n):
    time.sleep(1)
    return f"Number = {n}"

numbers = [0,1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    t = time.time()
    with ProcessPoolExecutor(max_workers = 3) as executor:
        results = executor.map(print_num,numbers)
    for result in results:
        print(result)

    fin_time = time.time() - t
    print(fin_time)
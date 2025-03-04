#Used when 
#CPU bound tasks- tasks that are heavy on CPU usage(mathematical calculations, data processing)
#Parallel execution- Multiple chores of CPU
#its almost same as multi threading , only difference is processes runs independently in seperate memory spaces

import multiprocessing
import time

def squares():
    for i in range(5):
        time.sleep(1)
        print(f"Square:{i*i}")
def cubes():
    for i in range(5):
        time.sleep(1)
        print(f"Cube:{i*i*i}")

if __name__ == "__main__":        
    #Create 2 processes
    p1 = multiprocessing.Process(target=squares)
    p2 = multiprocessing.Process(target=cubes)

    t = time.time()
    #Start process
    p1.start()
    p2.start()

    #Wait for process to complete
    p1.join()
    p2.join()

    fin_time = time.time() - t
    print(fin_time)
from logger import logging

def add(a,b):
    
    logging.debug("The addition operation is occuring. ")
    return a+b

logging.debug("The addition function is called")
add(5,10)

#to run this python file first go into the proper directory in terminal then run "python test.py" command 

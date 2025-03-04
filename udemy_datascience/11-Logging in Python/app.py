import logging

logging.basicConfig(          
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),    #file name mentioned where all events are to be logged in
        logging.StreamHandler()             #this logs in all the messages into the mentioned file
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    res = a+b
    logger.debug(f"Adding {a}+{b} = {res}")
    return res
def sub(a,b):
    res = a-b
    logger.debug(f"Subtracting {a}-{b} = {res}")
    return res
def mul(a,b):
    res = a*b
    logger.debug(f"Multiplying {a}*{b} = {res}")
    return res
def div(a,b):
    try:
        res = a/b
        logger.debug(f"Dividing {a}/{b} = {res}")
        return res
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
    
add(5,6)
sub(4,7)
mul(2,8)
div(56,0)
        
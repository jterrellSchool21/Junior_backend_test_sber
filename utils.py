from time import time
import logging
import os

logging.basicConfig(filename=f"logging_for_tasks.log", level=logging.INFO, filemode='w+')
def time_for_function(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        delta = float(time() - start)
        logging.info(f"\tTime for {func.__name__} with args {args} = {delta:.6f}")
        return res
    return wrapper
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import time

# Alternative examples:
# 1. http://ipython.org/ipython-doc/dev/parallel/index.html
# 2. http://www.davekuhlman.org/python_multiprocessing_01.html
# 3. https://www.binpress.com/tutorial/simple-python-parallelism/121

def print_(x):
    print("Parallel hello! id: %i" % x)
    time.sleep(1)
    return x**2

if __name__ == '__main__':
    pool = Pool()
    vals = pool.map(print_, range(30))
    print(vals)
    
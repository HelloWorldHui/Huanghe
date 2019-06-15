# coding=utf
"""
author=Hui_T
"""

import time
import threading
def func(n):
    time.sleep(0.001)
    print(n+n)
if __name__ == '__main__':
    t_list = []
    first = time.time()
    for i in range(10000):

        t = threading.Thread(target=func,args=(i,))
        t_list.append(t)
        t.start()
    [tt.join() for tt in t_list]
    last = time.time()

    t_1 = time.time()
    for i in range(10000):
        func(i)
    t_2 = time.time()
    print(last - first)
    print(t_2-t_1)

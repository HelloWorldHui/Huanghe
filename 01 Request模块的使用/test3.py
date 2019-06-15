# coding=utf
"""
author=Hui_T
"""
# try:
#     print(1)
# finally:
#     print(2)
import queue
q = queue.Queue()
q.put(1)
q.put(2)
# print(q.get())
# print(q.get())
# print(q.get())
# ==
# while True:
#     url = q.get()
#     try:
#         print(url)
#     finally:
#         q.task_done()
# ===========
try:
    print(1)
    name
except :
    print('xx')
finally:
    print(2)
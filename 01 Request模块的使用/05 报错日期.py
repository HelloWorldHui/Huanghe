# coding=utf
"""
author=Hui_T
"""
import csv
with open('log1.csv','r',encoding='gbk') as f:
    # file  = csv.reader(f)
    # for i in file:
    #     print(i)
    for i in f:
        print(i.strip())
# =======================================
# import threading
# import queue
# def run(queue):
#     while 1:
#         print(queue.get())
#         queue.task_done()
# def run2(queue):
#     while 1 :
#         print(queue.get())
#         queue.task_done()
# if __name__ == '__main__':
#     q = queue.Queue()
#     for i in range(3):
#         t = threading.Thread(target=run,args=(q,))
#         t.setDaemon(True)
#         t.start()
#     for i in range(200):
#         q.put(i)
#     q.join()
#     print('---------------------------------------------------')
#     q2 = queue.Queue()
#     for i in range(2):
#         t2 = threading.Thread(target=run2,args=(q2,))
#         t2.setDaemon(True)
#         t2.start()
#     for i in range(200):
#         q2.put(i)
#     q2.join()
#     print(222222222222222222222222222222222222222222)
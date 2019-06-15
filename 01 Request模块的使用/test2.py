# coding=utf
"""
author=Hui_T
"""
import time

List1=['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
List2=['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
List3=['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
print(list(zip(List1,List2,List3)))
# [('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c'), ('a', 'b', 'c')]

l1 = [[1,2],[3,4]]
l2 = [[6,6],[7,7]]
print(list(zip(l1,l2)))
print(["",].extend([1])) # None ****************
l = [1]

t1 = time.time()
l.insert(0,"")
time.sleep(0.1)
print(l)
t2 = time.time()
print(t2-t1)

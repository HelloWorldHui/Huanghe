# coding=utf
"""
author=Hui_T
"""
import datetime
# d1 = datetime.datetime.now().strftime("%Y-%m-%d")
d1 = datetime.datetime.now()
d2 = datetime.datetime.strptime("2019-06-13", "%Y-%m-%d")
d  = datetime.timedelta(days=1)
while d1>d2:
    print(d2)
    d2+=d
print(d2,d1)
print(type(d2),type(d1))
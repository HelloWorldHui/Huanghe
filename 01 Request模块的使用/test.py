# coding=utf
"""
author=Hui_T
"""
from lxml import etree
# n  = 0.1
#
# print(n)         # 0.1
# print("%05d" %n) # 000000
# print("%.3f" %n) # 0.100
with open("table.html",'r',encoding='utf8') as f :
    s = f.read()
tree = etree.HTML(s)
s = tree.xpath("//div/table/tbody")
print(s)
# coding=utf
"""
author=Hui_T
"""
import pandas
from lxml import etree
# with open("table.html",'r',encoding="utf8") as f :
#     df = pandas.read_html(f.read())
with open("table.html",'r',encoding='utf8') as f :
    doc = f.read()
# print(doc)
tree = etree.HTML(doc)
table = tree.xpath(".//div/table")[0]
table = etree.tostring(table,method='html')
print(table)
df = pandas.read_html(table)
print(df[0])
excel = pandas.ExcelWriter("table.xlsx")
df[0].to_excel(excel)
excel.close()

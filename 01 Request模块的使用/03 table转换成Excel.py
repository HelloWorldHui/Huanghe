# coding=utf
"""
author=Hui_T
"""
import pandas
with open("table.html",'r',encoding="utf8") as f :
    df = pandas.read_html(f.read())
print(df[0])
excel = pandas.ExcelWriter("table.xlsx")
df[0].to_excel(excel)
excel.close()

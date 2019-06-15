# coding=utf
"""
author=Hui_T
"""
import requests
url = "https://www.baidu.com/s"
# 请求头,带参数  百度搜索url

response = requests.get(url=url,params={"wd":"python"},headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"})
# wd 搜索的关键字  UA(User-Agent)反爬

with open("baidu.html","w",encoding="utf8") as f:
    f.write(response.text)
# result.content bytes形式
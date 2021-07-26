import requests
import re
import csv

url="https://movie.douban.com/top250"
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"}
resp=requests.get(url,headers=header)
resp.encoding=resp.apparent_encoding
page_content=resp.text#页面源代码
#解析数据
obj=re.compile(r'<li>.*?<span class="title">(?P<name>.*?)'
               r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
               r'.*?<span>(?P<number>.*?)人评价</span>',re.S)
result=obj.finditer(page_content)

with open("data.csv",mode="w",encoding="utf-8",newline='') as f:
    csvwriter=csv.writer(f)
    for it in result:
        print(it.group("name"))
        print(it.group("score"))
        print(it.group("number"))
        print(it.group("year").strip())
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
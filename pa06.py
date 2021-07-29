#爬电影天堂
#定位到2021必看片

import requests
import re

domain="https://www.dytt8.net/"
resp=requests.get(domain,verify=False)#verify=False去掉安全验证
resp.encoding=resp.apparent_encoding
# print(resp.text)
obj1=re.compile(r"2021新片精品.*?<ul>(?P<rl>.*?)</ul>",re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'片　　名　(?P<name>.*?)<br />.*?<br /><a target="_blank" '
                r'href="(?P<href2>.*?)">',re.S)
result=obj1.finditer(resp.text)
child_href_list=[]
for it in result:
    ul=it.group("rl")
    result2=obj2.finditer(ul)
    count=0
    for itt in result2:
        count+=1
        child_href=domain+itt.group("href").strip("/")
        if count!=1:
          child_href_list.append(child_href)
        # print(child_href)

for href in child_href_list:
    child_resp=requests.get(href)
    child_resp.encoding=child_resp.apparent_encoding
    # print(href)
    result3=obj3.search(child_resp.text)
    print(result3.group("name"))
    print(result3.group("href2"))


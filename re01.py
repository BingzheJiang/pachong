#re模块

import re
#findall:匹配字符串中所有的符合正则的内容，
list=re.findall(r"\d+","我的电话是:1515，我女朋友的电话是:168295")
print(list)

#finditer:匹配字符串中所有的内容，返回的是迭代器，效率高
it=re.finditer(r"\d+","我的电话是:1515，我女朋友的电话是:168295")
for i in it:
    print(i)
    print(i.group())

#serch，找到一个结果就返回，返回的结果是match对象，那数据需要.group()
#
s=re.search(r"\d+","我的电话号是：10086，我女朋友的电话是：10010")
print(s.group())

#match:从头开始匹配
s=re.match(r"\d+","10086，我女朋友的电话是：100")
print(s.group())


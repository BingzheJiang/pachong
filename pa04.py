import requests

url="https://movie.douban.com/j/chart/top_list"
#重新封装参数
param={
    "type": "24",
    "interval_id": "100:90",
    "action":"",
    "start": "0",#通过改变这个数来实现换页
    "limit": 20
}
header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
resp=requests.get(url,params=param,headers=header)
# print(resp.request.headers)
# print(resp.text)
print(resp.json())
resp.close() #关闭resp
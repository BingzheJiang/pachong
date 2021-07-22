#百度翻译
import requests

url="https://fanyi.baidu.com/sug"
data={'kw':'hello'}
resq=requests.post(url,data=data)
#发送post请求，发送的数据必须放在字典中，通过data参数进行传递
print(resq.json())#将服务器返回的内容直接处理成json
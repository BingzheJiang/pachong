#百度搜索
import requests

query=input("请输入；")
url=f"https://www.baidu.com/s?ie=UTF-8&wd={query}"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
resp=requests.get(url,headers=headers)
resp.encoding=resp.apparent_encoding
print(resp.text)
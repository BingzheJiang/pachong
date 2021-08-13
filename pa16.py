#m3u8视频爬取简单版
import requests
import re

# url="https://www.91kanju.com/vod-play/54812-1-1.html"
# resp=requests.get(url)
# # print(resp.text)
# obj=re.compile(r"url: '(?P<url>.*?)',",re.S)
# m3u8_url=obj.search(resp.text).group("url")
# print(m3u8_url)
# resp.close()
#
# #下载m3u8文件
# resp2=requests.get(m3u8_url)
# with open("move/zherenwanghou.m3u8",mode="wb") as f:
#     f.write(resp2.content)
# resp2.close()
# print("下载完毕")

#解析m3u8文件
n=1
with open("move/zherenwanghou.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()#先去掉空白，空格，换行符
        if line.startswith("#"):
            continue
        print(line)
        resp3=requests.get(line)
        f=open(f"move/{n}.ts",mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1

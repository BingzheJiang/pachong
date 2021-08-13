#m3u8视频爬取复杂版
import requests
import re
import aiohttp
import aiofiles
import asyncio
from Crypto.Cipher import AES
import os

# "//player.yunb.tv/dplayer.php?url=https://vod8.wenshibaowenbei.com/20210726/xXZyENCI/index.m3u8"
# /20210726/xXZyENCI/1000kb/hls/index.m3u8
# https://vod8.wenshibaowenbei.com/20210726/xXZyENCI/1000kb/hls/index.m3u8
def download_m3u8(url,name):
    resp=requests.get(url)
    with open("movie02/"+name+".txt",mode="wb") as f:
        f.write(resp.content)

def get_m3u8_url(url):
    resp=requests.get(url)
    obj=re.compile(r'"link_pre":"","url":"(?P<url>.*?)"',re.S)
    m3u8_url=obj.search(resp.text).group("url")
    resp.close()
    m3u8_url=m3u8_url.replace('\\','')
    return m3u8_url

async def download_ts(url,session):
    async with session.get(url) as resp:
        async with aiofiles.open("movie02/"+url.split("hls")[1],mode="wb") as f:
            await f.write(await resp.content.read())
    print(url.split("hls")[1]+"下载完毕")

async def aio_download(src):
    tasks=[]
    async with aiohttp.ClientSession() as session:#提前准备好session
        async with aiofiles.open(src,mode="r",encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                else:
                    line=line.strip()
                    # print(line)
                    task=asyncio.create_task(download_ts(line,session))
                    tasks.append(task)
            await asyncio.wait(tasks)

def get_key(url):
    resp=requests.get(url)
    return resp.text

async def dec_ts(name,key):
    key=key.encode("utf-8")
    aes=AES.new(key=key,IV=b"0000000000000000",mode=AES.MODE_CBC)
    async with aiofiles.open(f"movie02/{name}",mode="rb") as f1:
        async with aiofiles.open("movie02/temp_"+name,mode="wb") as f2:
            bs=await f1.read()#从源文件读取到内容
            await f2.write(aes.decrypt(bs))
    print(f"{name}处理完毕")

async def aio_dec(key):
    tasks=[]
    async with aiofiles.open("movie02/m3u8第二层.txt",mode="r",encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line=line.strip()
            task=asyncio.create_task(dec_ts(line.split("hls/")[1],key))
            # print(line.split("hls")[1],key)
            tasks.append(task)
        await asyncio.wait(tasks)

def merge_ts():
    lst=[]
    with open("movie02/m3u8第二层.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line=line.strip()
            lst.append("movie02/temp_"+line.split("hls/")[1])
    s="+".join(lst)
    os.system(f"copy /b {s} movie.mp4")
    print("OK")
    # print(s)

def main(url):
    # m3u8_url=get_m3u8_url(url)
    # download_m3u8(m3u8_url,"m3u8第一层")
    # with open("movie02/m3u8第一层.txt",mode="r",encoding="utf-8") as f:
    #     for line in f:
    #         if line.startswith("#"):
    #             continue
    #         else:
    #             line=line.strip()
    #             second_m3u8_url=m3u8_url.split("/20210726")[0]+line
    #             download_m3u8(second_m3u8_url,"m3u8第二层")
    #下载视频，异步
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(aio_download("movie02/m3u8第二层.txt"))
    # https://ts8.hhmm0.com:9999/20210726/xXZyENCI/1000kb/hls/key.key
    # with open("movie02/m3u8第二层.txt",mode="r",encoding="utf-8") as f:
    #     obj=re.compile(r'URI="(?P<key>.*?)"',re.S)
    #     key=obj.search(f.read()).group("key")
    # key_str=get_key(key)#拿到秘钥
    # print(key_str)
    # #解密
    # loop.run_until_complete(aio_dec(key_str))
    #合并成mp4
    merge_ts()

if __name__=='__main__':
    url="https://www.yunbtv.com/vodplay/nishiwoderongyao-1-1.html"
    main(url)

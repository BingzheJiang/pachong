import aiohttp
import asyncio
import time
import requests

async def aiodownload(url,session):
    name=url.split('/')[-1]
    # 发送请求, 这⾥和requests.get()⼏乎没区别, 除了代理换成了proxy
    async with session.get(url) as resp:
        content=await resp.content.read()
        with open("img2/"+name,mode='wb') as f:
            f.write(content)
async def main():
    #创建session对象 -> 相当于requsts对象
    async with aiohttp.ClientSession() as session:
        tasks=[asyncio.create_task(aiodownload(url,session)) for url in urls]
        await asyncio.wait(tasks)

#同步⽅式下载图⽚
def download(url):
    name=url.split("/")[-1]
    resp=requests.get(url)
    content=resp.content
    with open("img2/"+name,mode='wb') as f:
        f.write(content)

urls=[
"    https://pit1.topit.pro/forum/202012/27/020533uym0jyjqymp4emmm.jpg",
    "https://pit1.topit.pro/forum/202012/27/020533pavn1nxcsa7nxcfa.jpg",
    "https://pit1.topit.pro/forum/202012/27/020533xwcqzd4e5k5pk5y5.jpg",
    "https://pit1.topit.pro/forum/202012/27/020533xaw9tavcw9hwepwp.jpg",
    "https://pit1.topit.pro/forum/202012/27/020533bg9dmamg0aspgikx.jpg",
    "https://pit1.topit.pro/forum/202012/27/020534gpd93ly39gpz0h5a.jpg"
]

if __name__=="__main__":
    # t2=time.time()
    # for url in urls:
    #     download(url)
    # print(time.time()-t2)
    t1=time.time()
    #异步爬虫
    # asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time()-t1)
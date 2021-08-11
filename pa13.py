#协程操作模板
import asyncio
import time

async def dowload(url):
    print("开始抓取")
    await asyncio.sleep(3)#模拟发送请求
    print("下载结束",url)

async def main():
    urls=[
        "http://www.baidu.com",
        "http://www.hhh.com"
    ]
    tasks=[dowload(url) for url in urls]
    done,pedding=await asyncio.wait(tasks)
    for d in done:
        print(d.result())

if __name__=='__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)
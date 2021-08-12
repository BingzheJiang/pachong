#爬百度小说，西游记
#所有章节的ID
# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
#
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}
import requests
import asyncio
import aiohttp
import json
import aiofiles

async def aiodownload(cid,b_id,title):
    data={
        "book_id":"4306063500",
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data=json.dumps(data)
    url=f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic=await resp.json()
            # print(dic['data']['novel']['content'])
            async with aiofiles.open("novel/"+title+".txt",mode='w',encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    resp=requests.get(url)
    # print(resp.json())
    dic=resp.json()
    tasks=[]
    for item in dic['data']['novel']['items']:
        title=item['title']
        cid=item['cid']
        tasks.append(aiodownload(cid,b_id,title))
    await asyncio.wait(tasks)

if __name__=='__main__':
    b_id="4306063500"
    url='http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+b_id+'"}'
    # getCatalog(url)
    asyncio.run(getCatalog(url))
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(getCatalog(url))
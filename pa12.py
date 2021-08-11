import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

def download_one_page(url):
    #拿到页面源代码
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    resp=requests.get(url,headers=header)
    html=etree.HTML(resp.text)
    # print(html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]/text()'))
    li=html.xpath("//ol[@class='grid_view']//li")
    for l in li:
        index=l.xpath("./div/div[1]/em/text()")[0]
        name=l.xpath("./div/div[2]/div[1]/a/span[1]/text()")[0]
        score=l.xpath(".//div[@class='star']//span[2]/text()")[0]
        info=[]
        info.append(index)
        info.append(name)
        info.append(score)
        csvwriter.writerow(info)
    print(url,"提取完毕!")
    # print(html.xpath('//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]'))
if __name__=="__main__":
    f=open("doubanpingfen250.csv",mode="w",encoding="utf-8",newline="")
    csvwriter=csv.writer(f)
    # for i in range(0,10):
    #     url=f"https://movie.douban.com/top250?start={i*25}&filter="
    #     download_one_page(url)
    with ThreadPoolExecutor(10) as t:
        for i in range(0,10):
            url=f"https://movie.douban.com/top250?start={i*25}&filter="
            t.submit(download_one_page,url)
    f.close()
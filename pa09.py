import requests
from lxml import etree

url="https://jinan.zbj.com/wzkf/f.html?&fr=newpdy.it.20.8.04"
resp=requests.get(url)
# print(resp.text)
html=etree.HTML(resp.text)
divs=html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div/div")
for div in divs:
    price=div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")
    print(price)
    number = div.xpath("./div/div/a[1]/div[2]/div[1]/span[2]/text()")
    print(number)

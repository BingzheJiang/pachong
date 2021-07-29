#爬图库
import requests
from bs4 import BeautifulSoup

l_quanju=[]
def download_img(child_url):
    r=requests.get(child_url)
    r.encoding = r.apparent_encoding
    c = BeautifulSoup(r.text, "lxml")
    src = c.find("div", class_="ImageBody").find("img").get('src')
    l_quanju.append(src)
    # print(src)

def down_src(src):
    with open("img/"+src.split("/")[-1],mode='wb') as f:
        r_img=requests.get(src)
        f.write(r_img.content)
        print(src,"down!")

url="https://www.umei.net/meinvtupian/"
resp=requests.get(url)
resp.encoding=resp.apparent_encoding
# print(resp.text)
main_page=BeautifulSoup(resp.text,"lxml")
alist=main_page.find("div",class_="TypeList").find_all("a")
# print(alist)
# print(type(alist))
list_=[]
for a in alist:
    href=a.get('href')
    child_url="https://www.umei.net"+href
    list_.append(child_url)
for child_url2 in list_:
    resp2 = requests.get(child_url2)
    resp2.encoding = resp2.apparent_encoding
    child_page = BeautifulSoup(resp2.text, "lxml")
    # print(child_url2)
    # print(child_page)
    alist2=child_page.find("div",class_="NewPages").find_all("a")
    download_img(child_url2)
    for a in alist2:
        href2=a.get('href')
        child_url3 = "https://www.umei.net" + href2
        download_img(child_url3)
        # print(child_url3)
    # print(list(set(l_quanju)))
    list_src=list(set(l_quanju))
    for it_src in list_src:
        down_src(it_src)





#爬index.html练习
from bs4 import BeautifulSoup

soup=BeautifulSoup(open('index.html'),'lxml')
# print(soup)
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)
print(type(soup.a))
print(soup)
import requests
from bs4 import BeautifulSoup

page=requests.get("https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ1.htm")
soup=BeautifulSoup(page.text,'html5lib')

last_link=soup.find(class_='AlphaNav')
last_link.decompose()

name_list=soup.find(class_='BodyText')
#print(name_list)
name_list_items=name_list.find_all('a')

"""
for i in name_list_items:
    print(i.prettify())
"""
for i in name_list_items:
    names=i.contents[0]
    print(names)
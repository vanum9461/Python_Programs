import requests
import html.parser
from bs4 import BeautifulSoup
import re

url='https://content.techgig.com/startups'
page=requests.get(url)

soup=BeautifulSoup(page.text,'html.parser')
'''
c=list()
l=len(soup.find_all('h3'))
print(l)

for i in soup.find(class_="article-list-blk"):
    print(soup.find_all('h3')[i].get_text())

'''

links = []
content2=[]
for link in soup.findAll('a'):
    links.append(link.get('href'))
#print(links)

length2=len(links)
for j in range(0,length2):
	if links[j]==None:
		pass
	elif re.findall(r'.cms$',links[j]):
		content2.append(links[j])
#print('______LINKS_1______',content2)
#print('',end='\n')
#print('______CONTS______')


for i in range(0,len(content2)):
	url1=content2[i]
	page=requests.get(url1)
	#page.status_code
	#page.text
	soup=BeautifulSoup(page.text,'html.parser')
	head=soup.find_all('div',class_=' ')
	para=[]
	for h in head:
		para=h.find_all('p')
	length=len(para)
	cont=[]
	for b in range(0,length-5):
		cont.append(para[b].get_text())
	#printing articles (cont)
	print(cont)
	print('',end='\n')

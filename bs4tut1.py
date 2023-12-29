import requests
from bs4 import BeautifulSoup


URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 
#print(r.content) 
soup=BeautifulSoup(r.content,'html5lib')
links=soup.find_all("a")
#print(links)
#print("\n")
print(soup.prettify())

"""
url="http://www.values.com/inspirational-quotes"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())
"""
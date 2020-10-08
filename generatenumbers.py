import requests
from bs4 import BeautifulSoup

def totalcase():
    url='https://www.worldometers.info/coronavirus/'
    r=requests.get(url)

    content=BeautifulSoup(r.text,'html.parser')
    content=content.find('div',class_='maincounter-number')
    content=content.find('span').text
    content=content.replace(",","")
    content=int(content)
    return content

def totaldeath():
    url='https://www.worldometers.info/coronavirus/'
    r=requests.get(url)

    content=BeautifulSoup(r.text,'html.parser')
    content=content.findAll('div',{'id':'maincounter-wrap'})
    death=content[1].span.text
    death=death.replace(",","")
    death=int(death)
    return death
    




    
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

with open("C:/Users/asus/OneDrive/Pictures/文档/webscraping/smartprix_Scraping/smartprixhtml1.html",'r',encoding='utf-8') as f:
    html=f.read()

soup=BeautifulSoup(html,'lxml')

cards=soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'})

name=[]
price=[]
spec_score=[]
sim=[]
processor=[]
ram=[]
battery=[]
display=[]
camera=[]
card=[]
os=[]
for i in cards:
    name.append(i.find('h2').text.strip())
    price.append(i.find('span',{'class':'price'}).text)
    spec_score.append(i.find('div',{'class':'tags'}).find('b').text)
    sim.append(i.find('ul',class_='sm-feat specs').find_all('li')[0].text)
    processor.append(i.find('ul',class_='sm-feat specs').find_all('li')[1].text)
    ram.append(i.find('ul',class_='sm-feat specs').find_all('li')[2].text)
    battery.append(i.find('ul',class_='sm-feat specs').find_all('li')[3].text)
    display.append(i.find('ul',class_='sm-feat specs').find_all('li')[4].text)
    try:
        camera.append(i.find('ul',class_='sm-feat specs').find_all('li')[5].text)
    except:
        camera.append(np.nan)
    try:
        card.append(i.find('ul',class_='sm-feat specs').find_all('li')[6].text)
    except:
        card.append(np.nan)
    try:
        os.append(i.find('ul',class_='sm-feat specs').find_all('li')[7].text)
    except:
        os.append(np.nan)


df=pd.DataFrame({
    'Model':name,
    'Price':price, 
    'Rating':spec_score,
    "Sim" : sim,
    'Processor':processor,
    'Ram':ram,
    'Battery':battery,
    'Display':display,
    'Camera':camera,
    'Card':card,
    "Os":os
})
# print(df)
# After creating df
df.to_csv("uncleaned_data.csv", index=False)
print("Data exported to smartprix_data.xlsx successfully!")
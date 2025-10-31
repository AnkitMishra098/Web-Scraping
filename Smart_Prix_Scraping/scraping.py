# Import necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# Load the saved HTML file from Smartprix
with open("C:/Users/asus/OneDrive/Pictures/文档/webscraping/smartprix_Scraping/smartprixhtml1.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup with lxml parser
soup = BeautifulSoup(html, 'lxml')

# Find all product cards on the page
cards = soup.find_all('div', {'class': 'sm-product has-tag has-features has-actions'})

# Initialize empty lists to store extracted data
name = []
price = []
spec_score = []
sim = []
processor = []
ram = []
battery = []
display = []
camera = []
card = []
os = []

# Loop through each product card and extract relevant details
for i in cards:
    # Extract model name
    name.append(i.find('h2').text.strip())
    
    # Extract price
    price.append(i.find('span', {'class': 'price'}).text)
    
    # Extract spec score (usually in bold inside 'tags' div)
    spec_score.append(i.find('div', {'class': 'tags'}).find('b').text)
    
    # Extract specs from the list (ul with class 'sm-feat specs')
    specs = i.find('ul', class_='sm-feat specs').find_all('li')
    
    # Extract each spec by position
    sim.append(specs[0].text)
    processor.append(specs[1].text)
    ram.append(specs[2].text)
    battery.append(specs[3].text)
    display.append(specs[4].text)
    
    # Use try-except to handle missing specs gracefully
    try:
        camera.append(specs[5].text)
    except:
        camera.append(np.nan)
    
    try:
        card.append(specs[6].text)
    except:
        card.append(np.nan)
    
    try:
        os.append(specs[7].text)
    except:
        os.append(np.nan)

# Create a DataFrame from the collected data
df = pd.DataFrame({
    'Model': name,
    'Price': price,
    'Rating': spec_score,
    'Sim': sim,
    'Processor': processor,
    'Ram': ram,
    'Battery': battery,
    'Display': display,
    'Camera': camera,
    'Card': card,
    'Os': os
})

# Export the DataFrame to a CSV file
df.to_csv("uncleaned_data.csv", index=False)

# Confirmation message
print("Data exported to smartprix_data.csv successfully!")

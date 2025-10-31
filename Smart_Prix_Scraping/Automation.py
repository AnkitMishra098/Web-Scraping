# Import necessary modules from Selenium and Python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver with the path to chromedriver
driver = webdriver.Chrome(service=Service("C:/Users/asus/OneDrive/Desktop/chromedriver.exe"))

# Open the Smartprix mobiles page
driver.get("https://www.smartprix.com/mobiles")
time.sleep(1)  # Wait for the page to load

# Apply the first filter (e.g., a brand or feature checkbox)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span').click()
time.sleep(1)

# Apply the second filter (e.g., another brand or feature)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()
time.sleep(1)

# Click the "Show More" or "Load More" button to load additional products
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()

# Get the initial scroll height of the page
old_height = driver.execute_script('return document.body.scrollHeight')

# Keep clicking "Load More" until no new content is loaded
while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(5)  # Wait for new content to load
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height, new_height)  # Debug: print scroll heights to track progress
    if new_height == old_height:
        break  # Exit loop if no new content is added
    old_height = new_height  # Update old height for next iteration

# Save the final HTML content of the page to a local file
html = driver.page_source
with open("Smart_prix_Scraping/smartprixhtml1.html", 'w', encoding='utf-8') as f:

    f.write(html)

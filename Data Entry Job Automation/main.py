import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')

links = soup.find_all(name="a", class_="property-card-link")
links_list = [link.get('href') for link in links]

prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
price_list = [price.text.split('+')[0].split('/')[0] for price in prices]

addresses = soup.find_all(name='address')
address_list = [address.text.strip().replace('|', '') for address in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/wRw1tYt8GjbL4LUZ6")
time.sleep(5)

for address, price, link in zip(address_list, price_list, links_list):
    input1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input1.send_keys(address)

    input2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input2.send_keys(price)

    input3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input3.send_keys(link)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(2)

    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(2)
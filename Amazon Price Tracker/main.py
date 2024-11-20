import os
import requests
import smtplib
from bs4 import BeautifulSoup


EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
URL = ('https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_2_mod_primary_new?'
       'sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-2')  # URL of the product from amazon


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8'
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price = float(soup.find(name='span', class_='a-price-whole').getText().split('.')[0].replace(',', ''))


subject = "Amazon Price Alert!"
body = f"Sony PlayStation®5 Console (slim) is now ₹{price}\n{URL}"
message = f"Subject: {subject}\n\n{body}"


with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="siddharthnarigra@gmail.com",
        msg=message.encode('utf-8')
    )
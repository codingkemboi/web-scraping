# Import required modules
import requests
from bs4 import BeautifulSoup
# ask input from the user
#coutry_name = str(input("Enter counrty name: "))


URL = "https://www.ooyyo.com/austria/used-cars-for-sale/c=CDA31D7114D3854F111B936FAA651453/"
response = requests.get(URL)

# Creating soap object
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('div', class_='beta')
for result in results:
    # Searching h2 tags having car names
    cars = result.find('h2').text
    # Searching div tags having basic-info class
    details = result.find('div', class_="basic-info").text.replace(' ', '')
    # printing the objects we have scraped in form of key and values
    print(f'Car Name:{cars}')
    print(f'Car Details:{details}')

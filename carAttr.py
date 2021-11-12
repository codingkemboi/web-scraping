# Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl.workbook import Workbook

# ask input from the user
#coutry_name = str(input("Enter counrty name: "))


# Make requests from webpage
URL = "https://www.ooyyo.com/germany/c=CDA31D7114D2854F111BFE6FAA651453/7565956744506322157.html/"
response = requests.get(URL)

# Creating soap object
soup = BeautifulSoup(response.content, 'html.parser')

# Searching div tags having columns class
results = soup.find_all('div', class_='columns')

# list to store data
car_name = []
basic_info = []
car_options = []
seller_contact = []


# Find the tags and get data from it
for result in results:
    # variables to store data
    name = result.find('h1').text
    car_name.append(name)

    info = result.find('ul', class_='basic-info').text
    basic_info.append(info)

    options = result.find('ul', class_="options").text
    car_options.append(options)

    seller_url = result.find_all("a")[1]["href"]
    seller_contact.append(seller_url)

    # try to display
    # print(f'Contact:{seller_url})

# Creating dataframe
df = pd.DataFrame({"Car Name": car_name})
df = pd.DataFrame({"Basic Information": basic_info})
df = pd.DataFrame({"Options": car_options})
df = pd.DataFrame({"Contact": seller_contact})

# Naming the columns
df.index = ['Name']
df.index = ['Details']
df.index = ['Options']
df.index = ['Contact']


# saving xlsx file
DATA = pd.ExcelWriter('carData.xlsx')
df.to_excel(DATA, index=False)

DATA.save()

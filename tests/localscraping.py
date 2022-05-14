import requests
from bs4 import BeautifulSoup
import re

traduccion = ".Q4iAWc"
sinonimos = ".Dwvecf"

# with open("./file.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

website = f'https://www.deepl.com/es/translator#en/es/here%0A%0A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

print(soup.find_all("span", {"class": "Q4iAWc"}))


with open("./file.html", "w") as file:
    file.write(str(soup))

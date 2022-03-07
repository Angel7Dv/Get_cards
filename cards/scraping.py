import requests
from bs4 import BeautifulSoup
import re

# leer cualquier web
website = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')


tags = soup.select('i, b , audio')
""" Extre las etiquetas que creemos que tiene el contenido importante"""

urls_text = re.compile(r'(?<=src=").*?(?=")|(?<=>").*?(?="<)') #
""" extrae la url de las etiquetas y el texto de una etiqueta"""

resultado = urls_text.findall(str(tags))
print(resultado)

# CREAR UN ARCHIVO CON LA INFORMACION
with open('phanteon.txt', 'w') as file: 
    file.write(str(resultado))
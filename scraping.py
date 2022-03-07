import requests
from bs4 import BeautifulSoup
import re
"""librerias: bs4 - requests - lxml """

# leer cualquier web
website = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
tags = soup.select('i, b , audio')


# EXTRER LOS ELEMENTOS DE UNA WEB
""" se recomienda buscar elementos en este orden = id > classname > tagname cssSelector > Xpath"""

# tags = soup.findAll(re.compile(r'(i)'))
# tags = soup.find_all(['i', 'b', 'audio' ])
# r = re.compile('(?<=src=").*?(?=")')
# audio='src="(.*?)"', text= '>"([^<>]*)"'

# content = open('cosa.txt', 'r')

# for i in content:
#     content = i




urls_text = re.compile(r'(?<=src=").*?(?=")|(?<=>)".*?"(?=<)') #


result = urls_text.findall(str(tags))
print(result)


# for line in tags:
#     #text = line.get_text()
#     string = str(line)
#     url = urls_text.findall(string)
#     print(url)


#print( text, audio , " \n")
#for i in soup:

"obtener todas las etiquetas audio y i dentro de content"

# audios = content.find_all('audio')

# CREAR UN ARCHIVO CON LA INFORMACION
with open('phanteon.txt', 'w') as file: 
    file.write(str(result))
import requests
from bs4 import BeautifulSoup
import re
"""librerias: bs4 - requests - lxml """

# leer cualquier web
website = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify()) # imprime todo el html de forma ordenada

# EXTRER LOS ELEMENTOS DE UNA WEB
""" se recomienda buscar elementos en este orden = id > classname > tagname cssSelector > Xpath"""


# tags = soup.select('i, b , audio')
# tags = soup.findAll(re.compile(r'(i)'))
tags = soup.find_all(['i', 'b', 'audio' ])

r = re.compile('(?<=src=").*?(?=")')

for line in tags:
    text = line.get_text()
    string = str(line)
    url = r.findall(string)
    
    print(text, url)
    # for i in line:
    #     string = str(i)
    #     data = r.findall(string)
    #     print("link=",data , "text =")
    #     # print(type(string))

        # audio = i["src"]
    
    # print(text )


#print( text, audio , " \n")
#for i in soup:

 

"obtener todas las etiquetas audio y i dentro de content"

# audios = content.find_all('audio')




# CREAR UN ARCHIVO CON LA INFORMACION
# with open(f'{titulo}.txt', 'w') as file: 
#     file.write(transcript)
import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator

# leer cualquier web
website = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')


# Obtenemos los audios y los textos en una lista
tags = soup.select('i, b , audio')
""" Extre las etiquetas que creemos que tiene el contenido importante"""
get_data = re.compile(r'(?<=src=").*?(?=")|(?<=>").*?(?="<)') #
""" extrae la url de las etiquetas y el texto de una etiqueta"""
resultado = get_data.findall(str(tags))


# Traduccion de textos
traductor = Translator()


# Agregamos los textos y audios a un dict
lista = []
objeto = {}
for i in resultado:
    if i.startswith("http") == True:
        """ si es una url agrega 1 elemento a un dic luego agrega ese dict a la lista"""
        objeto = {"url": i}
    else:
        
        # text = re.sub(r'[^\w]', ' ', i.lower())
        # text = " ".join(re.split(r"\s+", text))
        objeto["text"] = i
        objeto["esp"] = traductor.translate("cosa")
        print(objeto["esp"])
        # lista.insert(len(lista), objeto)
        # objeto.clear


    


# CREAR UN ARCHIVO CON LA INFORMACION
# with open('phanteon.txt', 'w') as file: 
#     file.write(str(lista))
import requests
from bs4 import BeautifulSoup
import re
import json
from deep_translator import GoogleTranslator
import csv


""" Obtiene una url y estrae los audios y los texto de las etiquetas que creemos que contienen los audios
    Crea un archivo Json a partir de esto
"""

name = "Illaoi"
url = "https://leagueoflegends.fandom.com/wiki/Pantheon/LoL/Audio"
tags = 'i, b , audio'


def get_cvs_donwload(card_name, typefile, data=[]):
    # with open(f'cards/{card_name}/{card_name}.json') as json_file:
        # data = json.load(json_file)

    new_data = []
    with requests.Session() as req:
        "! se abre una secion para hacer multiples descargas"
        
        for index, iten in enumerate(data):
            name = f'{card_name}_{index+1}{typefile}'
            print(f"Downloading File {name}")
            download = req.get(iten["url"])
            if download.status_code == 200: # si el status es 200 comienza la descarga
                with open(f'{card_name}/{name}', 'wb') as f:
                    f.write(download.content)
                    print(f"Success Download File {name}")
            else:
                print(f"Download Failed For File {name}")
            iten["audio"] = name
            new_data.insert(len(new_data), iten)

    with open(f'{card_name}/{card_name}.json', "w") as outfile:
        json.dump(new_data, outfile)

    # Creacion del cvs borrando la url
    for i in new_data:
        i["text"] = re.sub('\W+', ' ', i["text"]).lstrip().lower()
        i["audio"] = f'[sound:{i["audio"]}]'
        del i["url"]
    """Falta agregar los nombres de los archivos de audio"""


    #Crea el archivo CSV
    csv_file = f'{card_name}/{card_name}.csv'
    csv_columns = ['audio', 'text', 'esp']
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

    print("Completado")

def scraping(card_name, url, get_tags, typefile):
    # leer cualquier web
    website = url
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')


    # Obtenemos los audios y los textos en una lista
    tags = soup.select(get_tags)
    """ Extre las etiquetas que creemos que tiene el contenido importante"""
    get_data = re.compile(r'(?<=src=").*?(?=")|(?<=>").*?(?="<)') #
    """ extrae la url de las etiquetas y el texto de una etiqueta"""
    resultado = get_data.findall(str(tags))

    es = GoogleTranslator(source='auto', target='es')
    # Agregamos los textos y audios a un dict
    lista = []
    objeto = {}

    for i in resultado:
        """ si es una url agrega 1 elemento a un dic luego agrega ese dict a la lista"""
        if i.startswith("http") == True:
            objeto = {"url": i}
        else:
            # text = re.sub(r'[^\w]', ' ', i.lower())
            # text = " ".join(re.split(r"\s+", text))
            objeto["text"] = i
            # traduccion:
            objeto["es"] = es.translate(str(objeto["text"]))
            print(objeto["es"])
            lista.insert(len(lista), objeto) 
            objeto.clear

    get_cvs_donwload(card_name, lista, typefile, )
    # # CREAR UN ARCHIVO CON LA INFORMACION
    # with open(f'cards/{card_name}/{card_name}.json', "w") as outfile:
    #     json.dump(lista, outfile)
    



scraping(name, "https://leagueoflegends.fandom.com/wiki/Illaoi/LoL/Audio", tags, "ogg")
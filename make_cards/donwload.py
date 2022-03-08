import requests
from bs4 import BeautifulSoup
import re
import json

card_name = "Pantheon"
data = []
with open(f'{card_name}/{card_name}.json') as json_file:
    data = json.load(json_file)



file = ".ogg"
new_data = []
with requests.Session() as req:
    "! se abre una secion para hacer multiples descargas"
    
    for index, iten in enumerate(data):
        name = f'{card_name}_{index+1}{file}'


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

print("Completado")

# recuerda guardar los archivos en 
#   C:\Users\user\AppData\Roaming\Anki2\Usuario 1\collection.media 
# para usarlos en el deck

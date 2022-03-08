import json
import re
import csv

card_name = "Pantheon"

# open Json
data = []
with open(f'{card_name}/{card_name}.json') as json_file:
    data = json.load(json_file)

# Borra la url y formatea el texto español
for i in data:
    i["esp"] = re.sub('\W+', ' ', i["esp"]).lstrip()
    i["audio"] = f'[sound:{i["audio"]}]'
    del i["url"]
"""Falta agregar los nombres de los archivos de audio"""


# Crea el archivo CSV
csv_file = f'{card_name}/{card_name}.csv'
csv_columns = ['text', 'audio', 'esp']
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in data:
            writer.writerow(data)
except IOError:
    print("I/O error")

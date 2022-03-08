# Traduccion de textos
from deep_translator import GoogleTranslator
import json


card_name = "Pantheon"

# open Json
data = []
with open(f'{card_name}/{card_name}.json') as json_file:
    data = json.load(json_file)

# Translate Json
es = GoogleTranslator(source='auto', target='es')
new_object = []
for i in data:
    i["esp"] = es.translate(i["text"]) 
    new_object.insert(len(new_object), i)
    print(i)


# # CREAR UN ARCHIVO CON LA INFORMACION
with open(f'{card_name}/{card_name}.json', "w") as outfile:
    json.dump(new_object, outfile)

print("Completado")

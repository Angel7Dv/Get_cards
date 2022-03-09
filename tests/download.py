import json
import urllib3
import urllib
card_name = "Pantheon"

# open Json
data = []
with open(f'{card_name}/{card_name}.json') as json_file:
    data = json.load(json_file)

formato = ".ogg"
new_data = []


for index, i in enumerate(data):
    # print(index, i["url"])
    video_name = i["url"].split('/')[-1]
    print("Downloading file:%s" % video_name)
    # Copy a network object to a local file
    audio = f'[sound:{card_name}_{index}{formato}]'
    i["audio"] = audio

    urllib.urlretrieve(i["url"], f'{card_name}/{audio}')
    
    new_data.insert(len(new_data), i)

with open(f'{card_name}/{card_name}.json', "w") as outfile:
    json.dump(new_data, outfile)

print("Completado")

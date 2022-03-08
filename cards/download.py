import json
import urllib3




card_name = "Pantheon"

# open Json
data = []
with open(f'{card_name}/{card_name}.json') as json_file:
    data = json.load(json_file)

formato = ".ogg"
data_cvs = []
for index, i  in enumerate(data):
    # print(index, i["url"])
    video_name = i["url"].split('/')[-1]
    print("Downloading file:%s" % video_name)
    # Copy a network object to a local file
    urllib3.urlretrieve(i["url"], "tutorial2.mp4")

 
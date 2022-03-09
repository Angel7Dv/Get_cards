import json
import urllib3
import urllib
import requests


url = ""
file_name = "audio.mp3"



# open Json
with requests.Session() as req:
    "! se abre una secion para hacer multiples descargas"
    print(f"Downloading File {file_name}")
    download = req.get(url)
    if download.status_code == 200: # si el status es 200 comienza la descarga
        with open(f'{file_name}', 'wb') as f:
            f.write(download.content)
            print(f"Success Download File {file_name}")
    else:
        print(f"Download Failed For File {file_name}")

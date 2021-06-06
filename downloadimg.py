# projects

import requests

url = "Url Here"
get_image = requests.get(url)

path = ""

with open(path,"wb") as f:
    f.write(get_image.content)

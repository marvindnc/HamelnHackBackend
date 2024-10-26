from jproperties import Properties
from imageToText import *
import json

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

model_url = configs.get("HOST_LLAVA").data
categories = configs.get("CATEGORIES").data

result = getAnswerFromLlava(model_url, "https://sensoneo.com/wp-content/uploads/2023/02/global-waste-index-2022-1024x536-1.png")

for cat in categories:
    json.loads(cat)
    print(category['name'])
    name = category['name']
    print(contains_word(result, name))

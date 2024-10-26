from jproperties import Properties
from imageToText import getAnswerFromLlava
import jsons

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

model_url = configs.get("HOST_LLAVA").data
category = jsons.load(configs.get("CATEGORY").data)
#print(jsons.dumps(category))

getAnswerFromLlava(model_url, "https://sensoneo.com/wp-content/uploads/2023/02/global-waste-index-2022-1024x536-1.png")

#name = category['name']

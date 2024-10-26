from jproperties import Properties
from imageToText import *
import json

configs = Properties()
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

model_url = configs.get("model").data
categories = configs.get("classes").data
print(categories)

#get image from database

result = getAnswerFromLlava(model_url, "https://sensoneo.com/wp-content/uploads/2023/02/global-waste-index-2022-1024x536-1.png")

categoriesArray = categories.split(",")
for cat in categoriesArray:
    print(cat)
    if (contains_word(result, cat)):
        print("detected")
        break
        #write to database with classification

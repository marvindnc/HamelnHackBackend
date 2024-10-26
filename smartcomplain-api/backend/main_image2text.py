from imageToText import *
import os

model_url = os.environ['LLM_MODEL']
img_classes = os.environ['IMG_CLASSES']
print(img_classes)

#get image from database

result = getAnswerFromLlava(model_url, "https://sensoneo.com/wp-content/uploads/2023/02/global-waste-index-2022-1024x536-1.png")

img_classes_array = img_classes.split(",")
for img_class in img_classes_array:
    print(img_class)
    if (contains_word(result, img_class)):
        print("detected")
        break
        #write to database with classification

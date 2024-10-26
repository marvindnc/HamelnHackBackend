import requests
import os

def getAnswerFromLlava(url: str, image: str) -> str:
    
    json_data = {
    "model": "llava",
    "prompt": "What is this image: " + image,
    "stream": False
    }
    response = requests.post(url, json=json_data)
    data = response.json()['response']
    print(data)
    return data

def contains_word(text, word):
    return (' ' + word.lower() + ' ') in text.lower()

def getImageClass(image_url:str) -> str:
    model_url = os.environ['LLM_MODEL']
    img_classes = os.environ['IMG_CLASSES']
    print(img_classes)

    result = getAnswerFromLlava(model_url, image_url)
    img_classes_array = img_classes.split(",")
    for img_class in img_classes_array:
        print(img_class)
        if (contains_word(result, img_class)):
            print("detected")
            break
            return img_class
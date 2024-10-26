import requests

def getAnswerFromLlava(url: str, image: str) -> str:
    
    json_data = {
    "model": "llava",
    "prompt": "What is this image: " + image,
    "stream": False
    }
    response = requests.post(url, json=json_data)
    data = response.json()['response']
    return data

def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')


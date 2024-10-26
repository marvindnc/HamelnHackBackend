from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response

from models import Info, ComplaintData, ComplaintGuess, ImageData

import os
import tempfile

import db_connect as db

app = FastAPI(
    title='smart complaint service',
    version='0.0.1',
    description='This is an API for the smart complaint app\n',
    servers=[{'url': 'http://localhost:8080/v0'}],
)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

contextPathBase = "/smartcomplaint"

complaints = []

# for Docker paths
baseImagePath = pathlib.Path(__file__).parent.resolve()

@app.get(contextPathBase + '/info', response_model=Info)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "smart complaint service"
    info.apiVersion = "0.0.1"
    return info

@app.get(contextPathBase + '/complaint', response_model=List[ComplaintData])
def get_info() -> List[ComplaintData]:
    return complaints

@app.post(contextPathBase + '/uploadimage/', response_model=ComplaintGuess)
async def create_upload_file(file: UploadFile):
    c = ComplaintData(description="test", image_id=1, capture_time=datetime.now())
    complaints.append(c)

    contents = await file.read()
    db.save_image(ImageData(image=contents, image_class="test", category="test"))
    return ComplaintGuess(guess="test", confidence=0.5)

@app.get(contextPathBase + '/images', response_model=List[ImageData])
def get_images() -> List[ImageData]:
    result = []
    db_images= db.get_images()
    for image in db_images:
        result.append(ImageData(image=image[1], image_class=image[2], category=image[3]))
    return result

@app.get(contextPathBase + '/image/{id}', response_model=bytes)
def get_image_as_file(id: int) -> bytes:
    im = db.get_image(id)
    return Response(content=im[1], media_type="image/jpg")

if __name__ == '__main__':
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']    
    db.connect(db_host, db_port)
    uvicorn.run('main:app', host="0.0.0.0", port=8001)
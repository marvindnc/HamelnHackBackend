from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response

from models import Info, ComplaintData, ComplaintGuess

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

@app.get(contextPathBase + '/info', response_model=Info)
def get_info() -> Info:
    info = Info()
    info.generation_date = datetime.now()
    info.systemDescription = "smart complaint service"
    info.apiVersion = "0.0.1"
    return info

@app.get(contextPathBase + '/complaint', response_model=List[ComplaintData])
def get_info() -> List[ComplaintData]:
    result = []
    complaints = db.get_complaints()
    for complaint in complaints:
        result.append(ComplaintData(description=complaint[1], capture_time=complaint[2], image=complaint[3], image_class=complaint[4], category=complaint[5]))
    return result

@app.post(contextPathBase + '/uploadimage/', response_model=ComplaintGuess)
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    c = ComplaintData(description="test", capture_time=datetime.now(), image=contents, image_class="", category=0)
    
    db.save_complaint(c)
    return ComplaintGuess(guess="test", confidence=0.5)

@app.get(contextPathBase + '/image/{id}', response_model=bytes)
def get_image_as_file(id: int) -> bytes:
    im = db.get_image(id)
    return Response(content=im[0], media_type="image/jpg")

if __name__ == '__main__':
    db_host = os.environ['DB_HOST']
    db_port = os.environ['DB_PORT']    
    db.connect(db_host, db_port)
    uvicorn.run('main:app', host="0.0.0.0", port=8001)
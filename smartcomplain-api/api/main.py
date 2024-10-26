from __future__ import annotations
from typing import List
from datetime import datetime
import pathlib

import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from models import Info, ComplaintData, ComplaintGuess

import tempfile

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
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + file.filename
    filename = pathlib.Path(tempfile.gettempdir(), filename)
    with open(filename, "wb") as buffer:
        contents = await file.read()
        buffer.write(contents)
    return ComplaintGuess(guess="test", confidence=0.5)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
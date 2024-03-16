import json
from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline

app = FastAPI()

class TextIn(BaseModel):
    text:str

class PredictionOut(BaseModel):
    response: str
    
@app.get("/")
def home():
    return {"health_check":"OK"}

@app.post('/',response_model=PredictionOut)
async def scoring_endpoint(item:TextIn):
    response = predict_pipeline(item.text)
    return {"response":response}

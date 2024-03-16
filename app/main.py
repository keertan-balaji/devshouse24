import json
from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from mangum import Mangum
app = FastAPI()
handler = Mangum(app)

class TextIn(BaseModel):
    text:str

class PredictionOut(BaseModel):
    response: str
    
@app.get("/")
def home():
    return {"health_check":"OK"}

@app.get('/',response_model=PredictionOut)
async def scoring_endpoint(item:TextIn):
    response = predict_pipeline(item.text)
    return {"response":response}

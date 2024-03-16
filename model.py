import tensorflow as tf
from keras_preprocessing.text import tokenizer_from_json 
from keras.preprocessing.sequence import pad_sequences
import json

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI() 
embed_size = 50 # how big is each word vector
max_features = 20000 # how many unique words to use (i.e num rows in embedding vector)
maxlen = 100 
with open('model/utils/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

class request(BaseModel):
    Message: str
@app.post('/')
async def scoring_endpoint(item:request):
    model = tf.keras.models.load_model('model\checkpoints\my_model.h5')
    x = str(item.model_dump()['Message'])
    sample_token = tokenizer.texts_to_sequences([x])
    sample_X_t = pad_sequences(sample_token, maxlen=maxlen)
    y = model.predict(sample_X_t,verbose=0)
    if y[0][1] > 0.5:
        return {"response":"toxic"}
    else:
        return {"response":"safe"}

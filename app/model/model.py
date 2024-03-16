import tensorflow as tf
from keras_preprocessing.text import tokenizer_from_json 
from keras.preprocessing.sequence import pad_sequences
import json
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import re
__version__ = "1.0"

embed_size = 50 # how big is each word vector
max_features = 20000 # how many unique words to use (i.e num rows in embedding vector)
maxlen = 100 

BASEDIR = Path(__file__).resolve(strict=True).parent

model = tf.keras.models.load_model(f'{BASEDIR}/checkpoints/my_model.h5')

with open(f'{BASEDIR}/utils/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

def predict_pipeline(text,model=model):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    sample_token = tokenizer.texts_to_sequences([text])
    sample_X_t = pad_sequences(sample_token, maxlen=maxlen)
    y = model.predict(sample_X_t,verbose=0)
    if y[0][1] > 0.5:
        return "toxic"
    else:
        return "safe"
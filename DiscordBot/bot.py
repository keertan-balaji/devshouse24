from discord import Intents, Client, Message
from typing import Final
import os
from dotenv import load_dotenv
import tensorflow as tf
from keras_preprocessing.text import tokenizer_from_json 
from keras.preprocessing.sequence import pad_sequences
import json
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import re
import warnings

warnings.filterwarnings("ignore")
__version__ = "1.0"

SENSITIVITY_THRESHOLD = 0.6
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
    if y[0][1] > SENSITIVITY_THRESHOLD:
        return "toxic"
    else:
        return "safe"

load_dotenv()
TOKEN: Final['os'] = os.getenv('DISCORD_TOKEN')


intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def analyze_message(user_message):
    result = predict_pipeline(str(user_message.content))
    if result == "toxic":
        await Message.delete(user_message)
        try:
            await user_message.author.send(f"Your message: {user_message.content} was deleted ny the bot as it goes against the serever's guidelines. Please ensure that you play a healthy role in the community.")
        except:
            pass

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    await analyze_message(message)

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()  
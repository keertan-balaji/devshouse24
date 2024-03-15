import sys, os, re, csv, codecs, numpy as np, pandas as pd
import tensorflow as tf
import keras
from keras_preprocessing.text import tokenizer_from_json 
from keras_preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers
from keras import initializers
import string
import json

embed_size = 50 # how big is each word vector
max_features = 20000 # how many unique words to use (i.e num rows in embedding vector)
maxlen = 100 

with open('model/utils/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)
embedding_matrix = np.load("model/utils/embedding_matrix.npy")

def create_model():
    model = tf.keras.Sequential([
        Input(shape=(maxlen,)),
        Embedding(max_features, embed_size),
        Bidirectional(LSTM(50, return_sequences=True, dropout=0.1, recurrent_dropout=0.1)),
        GlobalMaxPool1D(),
        Dense(50, activation="relu"),
        Dropout(0.1),
        Dense(2, activation="sigmoid"),
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

model = tf.keras.models.load_model('model\checkpoints\my_model.h5')

def predict(model,x:str):
    sample_token = tokenizer.texts_to_sequences([x])
    sample_X_t = pad_sequences(sample_token, maxlen=maxlen)
    y = model.predict(sample_X_t,verbose=0)
    print(y)

predict(model,"You're a funking dickhead")
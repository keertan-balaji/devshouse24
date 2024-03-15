import sys, os, re, csv, codecs, numpy as np, pandas as pd
import tensorflow as tf
import tensorflow.python.keras as keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers
import string

model = keras.models.load_model('model\checkpoints\offense_classification_v3')

print(model.summary())
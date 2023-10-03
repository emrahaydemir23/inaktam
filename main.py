import pandas as pd, urllib
from bs4 import BeautifulSoup
import streamlit as st, pickle, numpy as np

def predict(model, degerler):
    with open(f'{model}.pkl', 'rb') as f:
        classifier_model = pickle.load(f)
    vector = []
    for i in degerler.split(','): vector.append(int(i))
    prediction = classifier_model.predict([vector])[0]
    return prediction

parametre = st.experimental_get_query_params()
degerler = parametre["d"][0]
model = parametre["m"][0]

tahminSonucu = predict(model, degerler)
st.title("Tahmin Sonucu:  "+str(tahminSonucu))


st.markdown('[Geri Git](https://inaktam.erciyes.edu.tr/kararTahmini.aspx)')



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
veri = parametre["i"][0]
degerler, model = veri.split('|')[0], veri.split('|')[1]
#degerler = parametre["d"][0]
#model = parametre["m"][0]

sonuc = "Davacı Lehine"
tahminSonucu = predict(model, degerler)
if tahminSonucu == 1: sonuc = "Davalı Lehine"
st.title("Tahmin Sonucu:  "+sonuc)


st.markdown('[Geri Git](https://inaktam.erciyes.edu.tr/kararTahmini.aspx)')



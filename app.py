import streamlit as st
import requests
from streamlit_lottie import st_lottie
from tkinter import *
from tkinter import font

import PIL
from PIL import Image



st.set_page_config(page_title="Sociala medier MI/IRL", page_icon=":)")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#-----LOAD ASSETS------
lottie_instagram = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_2ks3pjua.json")
lottie_facebook = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_7akxvutj.json")
img_mi_ingolf = Image.open("images/mi_ingolf.png")
img_logo_trans = Image.open("images/1. Logo_svart_text_transparent_bakgrund.png")

#-----HEADER SECTION-----
st.write("##")
st.image(img_mi_ingolf)
st.subheader("Följ oss och få uppdateringar på vad som händer i studentlivet och heads up om framtida event.")

with st.container():
    st.write("---")

#------Links-----
left_column, right_column = st.columns(2)
with right_column:
    st.write("[Mälardalens Ingenjörer Facebook](https://www.facebook.com/Malardalensingenjorer)")
    st.write("[Ingolf Facebook](https://www.facebook.com/ingolf.mdi)")
with left_column:
    st_lottie(lottie_facebook,height=75,key="facebook")

left_column, right_column = st.columns(2)
with right_column:
    st.write("[Mälardalens Ingenjörer Instagram](https://instagram.com/mi.mdu_?igshid=YmMyMTA2M2Y=)")
    st.write("[Ingolf-IRL Instagram](https://instagram.com/ingolf.mdu?igshid=YmMyMTA2M2Y=)")

with left_column:
    st_lottie(lottie_instagram, height=75, key="instagram")
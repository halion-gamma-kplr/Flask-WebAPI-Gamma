import streamlit as st
import numpy as np
import time
import datetime
import pandas as pd

st.title("Mon application Streamlit avec Markdown")
st.subheader("Exemple d'utilisation du Markdown")
st.markdown("Voici un **texte en gras** et un *texte en italique*.")

st.markdown("""
Voici une liste à puces :
- élément 1
- élément 2
- élément 3
""")

st.markdown(""" Voici une liste numérotée :
1. élément 1
2. élément 2
3. élément 3
""")

st.markdown("> Voici une citation.")
st.markdown("---")
st.markdown("![Alt texte](https://img.freepik.com/photos-premium/adorable-mignon-chat-potele-rendu-3d_784625-1053.jpg)")
st.markdown("[Cliquez ici pour aller sur Google](https://www.google.com)")

if st.button(label='Clique-moi!') :
    st.write('Bouton cliqué!')

slider = st.slider('Arguments ordered no need to specify them',7, 28, 10, 3)
st.write(slider)

st.selectbox('ChooseOne',['cats', 'dogs', 'ducks', 'monkeys', 'parrots'],2)

st.multiselect('ChooseAsManyAsYouWant', ['cats', 'dogs', 'ducks', 'monkeys', 'parrots'])

text = st.text_input('TypingIsFun','Enter text')
st.write(text)

number = st.number_input('TypingValues', 0, 100, 42)
st.write(number)

big_text = st.text_area('MultiLineTyping', 'one line\ntwo lines\nanother line\nanother one\nand another one')
st.write(big_text)

date = st.date_input('EnterDate', datetime.date(2009,10,25))
st.write(date)

time = st.time_input('EnterTime', datetime.time(7,28,42))
st.write(time)

download = st.file_uploader('Selectionner un fichier à uploader')
df = pd.DataFrame(download)
st.line_chart(df,x='id',y='age')

st.checkbox(label='Check/Uncheck')




progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
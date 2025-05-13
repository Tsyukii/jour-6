#cd C:\Users\kevin\Documents\ESTP\Ingé_2A\IoT
#python jour5.py
#streamlit run jour5.py


print('hello')

import streamlit as st
import pandas as pd
st.write("hello world !")

#PRESENTATION
st.title("My streamlit app")
st.subheader("Try out the app")
st.text("This is a simple element")

#2 SIDEBAR
# Choix dans une liste déroulante (dans la sidebar)
graph_type = st.sidebar.selectbox("Iil Choisissez un type de graphique :", ["Ligne", "Barres", "Aucune"])
st.write(f"Vous avez choisi le type de graphique : {graph_type}")
         
#3 UPLOAD CSV FILE
uploaded_file = st.file_uploader(" Téléchargez un fichier (SV", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.write( "Voici un aperçu de votre fichier :")
    st. dataframe(df.head())

    #4 Affichage du graphique en fonction du type choisi 
    if graph_type == "Ligne":
        st. line_chart (df)
    elif graph_type == "Barres":
        st. bar_chart(df)
    else :
        st.write( "Aucun graphique, sélectionné.")

#4 SLider
age = st.slider("Quel âge avez-vous ?", 0, 100, 25)
st.write(f"Vous avez {age} ans.")

import numpy as np
# Checkbox
if st.checkbox("Afficher un tableau aleatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']))
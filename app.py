import streamlit as st
import numpy as np
import pandas as pd
import pickle



st.title('Predict quality of Fresh water!:wave:')

a = st.slider("pH value",0,14) 
b = st.number_input("Iron Value",step=1.,format="%.5f")
c = st.number_input("Nitrate Value",step=1.,format="%.5f")
d = st.number_input("Chloride Value",step=1.,format="%.5f")
e = st.number_input("Lead Value",step=1.,format="%.5f")
f = st.number_input("Zinc Value",step=1.,format="%.5f")

dic={'Colorless': 0, 'Faint Yellow': 1, 'Light Yellow': 2, 'Near Colorless': 3, 'Yellow': 4,'Other':5}
arr = list(dic.keys())
g = st.selectbox("Color",arr)
g = dic[g]

h = st.number_input("Turbidity Value",step=1.,format="%.5f")
i = st.number_input("Fluoride Value",step=1.,format="%.5f")
j = st.number_input("Copper Value",step=1.,format="%.5f")
k = st.number_input("Odor Value",step=1.,format="%.5f")
l = st.number_input("Sulfate Value",step=1.,format="%.5f")
m = st.number_input("Chlorine Value",step=1.,format="%.5f")
n = st.number_input("Manganese Value",step=1.,format="%.5f")
o = st.number_input("Total Dissolved Solids Value",step=1.,format="%.5f")

dice={'Aquifer': 0, 'Ground': 1, 'Lake': 2, 'Reservoir': 3, 'River': 4, 'Spring': 5, 'Stream': 6, 'Well': 7,'Other': 8}
arr = list(dice.keys())
p = st.selectbox("Source",arr)
p = dice[p]

new_dice = {'XGBoost':1,'Logistic Regression':2}
new_arr = list(new_dice.keys())
q = st.selectbox("ML MODEL",newarr)
if q == 1:
    file = open('intel_smit.pkl','rb')
else:
    file = open('intel_smit_logistic.pkl','rb')

model = pickle.load(file)

def predict(): 
    row = np.array([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])
    col=['pH','Iron','Nitrate','Chloride','Lead','Zinc','Color','Turbidity','Fluoride','Copper','Odor','Sulfate','Chlorine','Manganese','Total Dissolved Solids','Source']
    
    X = pd.DataFrame([row], columns = col)
    prediction = model.predict(X)
    if prediction[0] == 1: 
        st.success('Safe to Drink :thumbsup:')
    else: 
        st.error('Unsafe to Drink :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)

file.close()

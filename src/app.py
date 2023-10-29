import streamlit as st

from pickle import load
import streamlit as st

import pandas as pd

model = load(open("../models/decisiontreeregressor.pkl", "rb"))

st.title("Diamond Price - Model prediction")


        # carat = float(request.form["carat"])
        # cut = str(request.form["cut"])
        # color = str(request.form["color"])
        # clarity = str(request.form["clarity"])
        # depth = float(request.form["depth"])
        # table = float(request.form["table"])
        # x = float(request.form["x"])
        # y = float(request.form["y"])
        # z = float(request.form["z"])

carat = st.slider("carat", min_value = 0.2, max_value = 5.01, step = 0.01)
cut = st.selectbox("Choose a cut:", ['Fair', 'Good', 'Ideal', 'Premium', 'Very Good'])
color = st.selectbox("Choose a color:", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox("Choose a clarity:", ['I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2'])
depth = st.slider("depth", min_value = 40, max_value = 80, step = 1)
table = st.slider("table", min_value = 40, max_value = 100, step = 1)
x = st.slider("x", min_value = 0.0, max_value = 11.0, step = 0.01)
y = st.slider("y", min_value = 0.0, max_value = 60.0, step = 0.1)
z = st.slider("z", min_value = 0.0, max_value = 10.0, step = 0.01)

if st.button("Predict"):
    colums = ['carat','cut','color','clarity','depth','table','x','y','z']
    data = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=colums)
    prediction = str(model.predict(data)[0])    
    st.write("Prediction:", prediction)
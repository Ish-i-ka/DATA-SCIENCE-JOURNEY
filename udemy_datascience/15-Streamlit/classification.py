import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data           #this cache is used so that each time we run this code the data is loaded from cache and not from the library evry time
def load_data():        #data is loaded into iris
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] =iris.target      #setting the target feature
    return df,iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()        #naming the classification model as model
model.fit(df.iloc[:,:-1],df['species']) #first parameter is independent feature and 2nd is dependent feature

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data =[[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predict_species = target_names[prediction[0]]

st.write("Prediction")
st.write(f"The predicted species is: {predict_species}")
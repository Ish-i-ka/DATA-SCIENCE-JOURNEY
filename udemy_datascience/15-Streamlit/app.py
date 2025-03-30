import streamlit as st 
import pandas as pd
import numpy as np

#title
st.title("Hello streamlit")

#Display simple text
st.write("This is simple text")

#create a dataframe
df = pd.DataFrame({
    "first col": [1,2,3,4],
    "second col": [10,20,30,40]
})

#Display dataframe
st.write("Here is the Dataframe")
st.write(df)

#create line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
import streamlit as st 
import pandas as pd
import numpy as np

df=pd.read_csv("tips.csv")
st.header('# st.dataframe')
st.caption('Display a df as an interactive table')
st.dataframe(data=df,width=1098,height=100)
st.markdown('# table')
st.table(df.head(5))
st.markdown('# json')
st.json(df.head(5).to_dict())
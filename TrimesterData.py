import streamlit as st
import pandas as pd

footballdata = pd.read_csv("FirstTrimesterCCData.csv")

st.dataframe(footballdata)

st.line_chart(data=footballdata, x= 'Down', y= 'Field Position')

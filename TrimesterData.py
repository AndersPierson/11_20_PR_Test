import streamlit as st
import pandas as pd
import altair as alt

footballdata = pd.read_csv("FirstTrimesterCCData.csv")

st.dataframe(footballdata)

st.linechart(data=footballdata, x='QB#', y='J#')


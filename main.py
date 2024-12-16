from io import StringIO
from polars import dataframe
import streamlit as st 
import polars as pl

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    dataframe = pl.read_csv(uploaded_file)

    edited_df = st.data_editor([
        {
            "column": x,
            "null_values": dataframe[x].null_count(),
            "drop_column": False,
            "remove_null": False,
         } for x in dataframe.columns
    ])

    if st.button("Perform"):
        for x in edited_df: 
            if x["remove_null"]:
                dataframe[x["column"]].drop_nulls()
            if x["drop_column"]:
                dataframe.drop(x["column"])
        dataframe.columns = [x["column"] for x in edited_df]

    st.write(dataframe.head(10))
    st.write(dataframe.tail(10))
    st.write(dataframe.describe())

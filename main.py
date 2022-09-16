
import numpy as np
import pandas as pd
import streamlit as st
import streamlit_pandas_profiling  as spp
import pandas_profiling as pp

header = st.container()

with header:
    st.markdown('''
# **The Data Analytics EDA App**

This little app will help you visualise any of your CSV files. Go ahead and give it a try.

 The app is built by combining `Pandas Profiling` and `Streamlit`.   
      
 Author -`Dilip Nikhil`
''')
sidebar = st.container()

with sidebar:
    st.sidebar.header("1. Upload your csv data")
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = pp.ProfileReport(df,explorative=True)
    with header:
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('-------')
        st.header('**Pandas Profiling Report')
        spp.st_profile_report(pr)
else:
    st.info("Waitinf for CSV file to be uploaded")
    if st.button('Press to use an example Dataset that is generated through numpy'):
        @st.cache
        def load_data():
            data = pd.DataFrame(np.random.rand(100,5),columns=["a","b","c","d","e"])
            return data
        df = load_data()
        pr = pp.ProfileReport(df,explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        spp.st_profile_report(pr)
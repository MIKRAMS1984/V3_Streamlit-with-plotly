import pandas as pd
import plotly
import plotly.express as px
import streamlit as st
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import profile_report
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report

# web app title
st.markdown('''
            # **EDA web app**
            This is the **EDA web app** created in Streamlit using **pandas-profiling** library.
            ''')

# how to upload a file from pc.
with st.sidebar.header('upload ur data csv file.'):
    uploaded_file = st.sidebar.file_uploader('upload your file', type=['csv'])
    df = sns.load_dataset('titanic')
    #st.sidebar.markdown('')
    #[Example cSV file](pdf)
    
# profiling report for pandas.
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv  = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('***Input DF***')
    st.write(df)
    st.write('....')
    st.header('**Profile report display**')
    st_profile_report(pr)
else:
    st.info('upload file.')
    if st.button('press to use example data')
    
    def load_data():
        a = pd.DataFrame(np.random.rand(100, 5), columns=['age', 'banana', 'kodanis', 'ear', 'eye'])
        return a
    df = load_data()
            
            




import streamlit as st
from existing import exist
from add_patient import enter_new_data
import pandas as pd

def load_data():
   
    data=pd.read_csv("./stage_1_balanced.csv",sep=';')
    return data

data=load_data()
st.set_page_config(page_title="webapp",page_icon=":tada:")
while(True):   
    

    action= st.sidebar.selectbox("Predict for", ("Existing patient", "Add Patient"))
    data_1=data
    if action == "Add Patient":
        
        
        data=enter_new_data(data_1)
        st.write(data.tail(1))
        
    else:
        st.write(data_1.tail(1))
        data=exist(data_1)
        
    
    

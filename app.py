import streamlit as st
from existing import exist
from add_patient import enter_new_data
import pandas as pd
import csv

def load_data():
   
    data=pd.read_csv("stage_1_balanced.csv",sep=';',index_col=False)
    # data=pd.DataFrame()
    # with open("./stage_1_balanced",'wr') as file:
    #     csvreader=csv.reader(file,delimiter=";")
    #     for row in csvreader:
    #         data.loc[len(data.index)]=row
    return data
print("Data")
data=load_data()
st.set_page_config(page_title="webapp",page_icon=":tada:")
  
    

action= st.sidebar.selectbox("Choose option", ("Predict", "Add Patient","Explanation"))

data.rename(columns={'Unnamed: 0': 'ID'},inplace=True)
if action == "Predict":
    
       # data=enter_new_data(data)
        #st.write(data.tail(1))
        
        
        data=exist(data)
        
        
     
elif action=="Add Patient":
    
    data=enter_new_data(data)
    data.to_csv("stage_1_balanced.csv",sep=';',index=False)
else:
    st.write("Global Explanation")
    
    

    

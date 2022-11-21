import streamlit as st
import pandas as pd
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from add_patient import enter_new_data
    
data=pd.read_csv("./stage_1_balanced.csv",sep=';')

st.set_page_config(page_title="webapp",page_icon=":tada:")
st.title("Machine Learning to predict ICU :wave:")
print(xgb.__version__)
with st.container():
    st.write("---")
    age = st.slider("Choose your age: ", min_value=16,   
                       max_value=66, value=35, step=1)
    st.write(data[data['ICU']==0].head(10))
with st.container():
    st.write('---')
    st.subheader("Enter id of patient")
    
    id_patient = st.text_input("Enter the id of patient")
    if id_patient == '':
        id_patient =0
    else:
        id_patient=int(id_patient)
    
    if(data[data['Unnamed: 0']==id_patient].empty):
        st.write("The patient with this id doesnt exist.Do you want to add patient?")
        if st.button("Add patient"):
            enter_new_data(data)
            #st.write("Hello")
            
    else: 
        st.write(data[data['Unnamed: 0']==id_patient])
        data_new = data[data['Unnamed: 0']==id_patient]
        data_new.drop(columns=['Unnamed: 0', 'ICU'],inplace=True)
        
        
        print("1")
        filename= "my_model2.pkl"
        model = pickle.load(open(filename,'rb'))
        print("2")        
        
        ICU = model.predict(data_new)
        print("3")
        st.write(f"My prediction is {ICU}")

    
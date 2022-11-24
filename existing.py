import streamlit as st
import pandas as pd
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from add_patient import enter_new_data
import streamlit.components.v1 as components
import shap
from draw import st_shap



# def load_data():
   
#     data=pd.read_csv("./stage_1_balanced.csv",sep=';')
#     # data=pd.DataFrame()
#     # with open("./stage_1_balanced",'wr') as file:
#     #     csvreader=csv.reader(file,delimiter=";")
#     #     for row in csvreader:
#     #         data.loc[len(data.index)]=row
#     return data

def exist(data):    
    

    #data=load_data()
    st.title("Machine Learning to predict ICU :wave:")
    print(xgb.__version__)
        
    with st.container():
        st.write('---')
        st.subheader("Enter id of patient")
        
        id_patient = st.text_input("Enter the id of patient")
        if id_patient == '':
            id_patient =0
        else:
            id_patient=int(id_patient)
        
        if(data[data['ID']==id_patient].empty):
            st.write("The patient with this id doesnt exist.Do you want to add patient?")
           
           
            return data
        
               
                
        else: 
            
            st.write(data[data['ID']==id_patient])
            data_new = data[data['ID']==id_patient]
           
            data_1=data_new.drop(columns=['ID', 'ICU'])
           
            
            
            filename= "my_model2.pkl"
            model = pickle.load(open(filename,'rb'))
                
          
            ICU = model.predict(data_1)
            #st.write(data_new)
            st.write(f"My prediction is {ICU}")
            with st.container():
                #t=data[data['Unnamed: 0']==id_patient]
                k=data.index[data['ID']==id_patient].tolist()
                k=k[0]
                X_test=data.drop(columns=['ID','ICU'])
                print("K ",k)
                explainer = shap.Explainer(model)
                shap_values=explainer(X_test)
                st.write("---")
                st.write("SHAP Value")
                st_shap(shap.plots.waterfall(shap_values[k]),400)
                st_shap(shap.plots.force(shap_values[k],link="logit"),400)
                st_shap(shap.plots.force(shap_values[k]),400)
                expected=explainer.expected_value
                st_shap(shap.decision_plot(expected,shap_values[k].values,X_test),400)
                
        
                return data

        

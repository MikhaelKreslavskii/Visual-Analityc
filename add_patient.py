import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
import shap
from draw import st_shap

def enter_new_data(data):
    
    d={}
    st.header("Add new Patient")
    for col in data.columns:
        d[col]=0
    id= st.number_input("Enter id of new patient",format="%d",step=1) 
    if not(data[data['ID']==id].empty):
        st.write("This ID has already exist")
    else:
        d["ID"]=id
    bmi = st.number_input("Enter bmi")
    d["BMI"]=bmi
    
    age = st.slider("Choose patinet age ", min_value=0,   
                       max_value=100, value=35, step=1)
    d["AGE"]=age
    rad=st.radio(
    "Sex",
    ('Male', 'Female'))
    if rad=='Male':
        sex=0
    else:
        sex=1
    d["SEX"]=sex
    
    alcohol_units_week = st.number_input("Enter alcohol units week")
    d["ALCOHOL_UNITS_WEEK"]=alcohol_units_week
    data_copy=data.drop(columns=['ICU'])
    #print(data.drop(columns=["ICU"],inplace=True))
    print(data.shape)
    alcoholcom = st.number_input("Enter alcoholcom")
    d["ALCOHOLCOM"]=alcoholcom
    alcoholyea= st.number_input("Enter alcoholyea")
    d["ALCOHOLYEA"]=alcoholyea
    yearabstin=st.number_input("Enter yearabstin")
    d["YEARABSTIN"]=yearabstin
    asa=st.number_input("Enter ASA")
    d["ASA"]=asa
    diabetsap=st.number_input("Enter diabetsap")
    d["DIABETESAP"]=diabetsap
    diabetsne=st.number_input("Enter diabetsne")
    d["DIABETESNE"]=diabetsne
    familiarca=st.number_input("Enter familiarca")
    d["FAMILIARCA"]=familiarca
    familiar_a= st.number_input("Enter familiar_a")
    d["FAMILIAR_A"]=familiar_a
    genealtera= st.number_input("Enter genealtera")
    d["GENEALTERA"]=genealtera
    numberprev=st.number_input("Enter numberprev")
    d["NUMBERPREV"]=numberprev
    parasitinf= st.number_input("Enter parasitinf")
    d["PARASITINF"]=parasitinf
    PCRONICAETIOLOGY=st.number_input("Enter PCRONICAETIOLOGY")
    d["PCRONICAETIOLOGY"]=PCRONICAETIOLOGY
    packyear=st.number_input("Enter packyear")
    d["PACKYEAR"]=packyear
    CIGARRETEP=st.number_input("Enter CIGARRETEP")
    d["CIGARRETEP"]=CIGARRETEP
    SMOKINGYEA=st.number_input("Enter SMOKINGYEA")
    d["SMOKINGYEA"]=SMOKINGYEA
    ETIOLOGYFI=st.number_input("Enter ETIOLOGYFI")
    d["ETIOLOGYFI"]=ETIOLOGYFI
    hoursadmisspain=st.number_input("Enter hoursadmisspain")
    d["HOURSADMISSPAIN"]=hoursadmisspain
    APCRITER_A =st.number_input("Enter APCRITER_A")
    d["APCRITER_A"]=APCRITER_A
    multisel=st.multiselect("Options: ", ['BACTERIALI','COLICBEFOR','PREVIOUSPA','HTA'
                                          'CARDIO','DYSLIPID','RESP_PREVIOUSDISEA','RENALCRONI',
                                          "HISTORY_CHOLECYSTECTOMY ","HEREDPANCR",
                                          'PREVIOUS_A',"SMOKING","STONESHIST","TRYGLICERI","VIRUSTYPE",
                                          "IPMN_global","ANTIARRITMICO","ANTIINFLAMATORIO",
                                          "BETABLOQUEANTES","DIURETICO","IECA","ANTICOAGULANTE","ANTIPLAQUETARIO",
                                          "ANTIDIABETICO","ESTATINA","BRONCODILATADORES",
                                          "ANTIDEPRESIVOS"])
    #data.loc[len(data.index)]=d.values
 
    st.write("Type of cancer")
    

   
    #data.loc[len(data.index)]=ar
    for col in data.columns:
        if col in multisel:
            d[col]=1
   # st.write(data.head(1))
        
    CANCERHI_A_0 = int(st.checkbox("CANCERHI_A_0 "))
    d["CANCERHI_A_0"]=CANCERHI_A_0
    CANCERHI_A_Acute_Myeloid_Leukemia=int(st.checkbox("CANCERHI_A_Acute_Myeloid_Leukemia"))
    d["CANCERHI_A_Acute Myeloid Leukemia"]= CANCERHI_A_Acute_Myeloid_Leukemia
    CANCERHI_A_Bladder_Cancer=int(st.checkbox("CANCERHI_A_Bladder_Cancer"))
    d["CANCERHI_A_Bladder Cancer"]=CANCERHI_A_Bladder_Cancer
    CANCERHI_A_Breast_Cancer=int(st.checkbox("ANCERHI_A_Breast_Cancer"))
    d["CANCERHI_A_Breast Cancer"]=CANCERHI_A_Breast_Cancer
    CANCERHI_A_Colorectal_Cancer=int(st.checkbox("CANCERHI_A_Colorectal_Cancer"))
    d["CANCERHI_A_Colorectal Cancer"]=CANCERHI_A_Colorectal_Cancer
    CANCERHI_A_Colorectal_Cancer_Prostate_Cancer=int(st.checkbox("CANCERHI_A_Colorectal_Cancer_Prostate_Cancer"))
    d["CANCERHI_A_Colorectal Cancer, Prostate Cancer"]=CANCERHI_A_Colorectal_Cancer_Prostate_Cancer
    CANCERHI_A_Endometrial_Cancer=int(st.checkbox("CANCERHI_A_Endometrial_Cancer"))
    d["CANCERHI_A_Endometrial Cancer"]= CANCERHI_A_Endometrial_Cancer
    CANCERHI_A_Gastric_Cancer=int(st.checkbox("CANCERHI_A_Gastric_Cancer"))
    d["CANCERHI_A_Gastric Cancer"]=CANCERHI_A_Gastric_Cancer
    CANCERHI_A_Haematological_Cancer=int(st.checkbox("CANCERHI_A_Haematological_Cancer"))
    d["CANCERHI_A_Haematological Cancer"]=CANCERHI_A_Haematological_Cancer
    CANCERHI_A_Kidney_Cancer=int(st.checkbox("CANCERHI_A_Kidney_Cancer"))
    d["CANCERHI_A_Kidney Cancer"]=CANCERHI_A_Kidney_Cancer
    CANCERHI_A_Lung_Cancer=int(st.checkbox("CANCERHI_A_Lung_Cancer"))
    d["CANCERHI_A_Lung Cancer"]=CANCERHI_A_Lung_Cancer
    CANCERHI_A_Prostate_Cancer = int(st.checkbox("CANCERHI_A_Prostate_Cancer"))
    d["CANCERHI_A_Prostate Cancer"]=CANCERHI_A_Prostate_Cancer
    CANCERHI_A_Rectal_Cancer = int(st.checkbox("CANCERHI_A_Rectal_Cancer"))
    d["CANCERHI_A_Rectal Cancer"]=CANCERHI_A_Rectal_Cancer
    CANCERHI_A_Thyroid_Cancer = int(st.checkbox("CANCERHI_A_Thyroid_Cancer"))
    d["CANCERHI_A_Thyroid Cancer"]=CANCERHI_A_Thyroid_Cancer
    #d["ICU"]=0
    print(len(d))
    #st.write(data.head(10))
    if st.button("Add patient"):
        filename="my_model2.pkl"
        model = pickle.load(open(filename,'rb'))
       
        #data.loc[len(data.index)]=list(map(lambda x: 0, data.columns))
        #st.write(data[-1])
        data_copy=data.append(d,ignore_index=True)
        #st.write(data.copy.shape())
        #data_copy.to_csv("stage_1_balanced.csv")
        #st.write(data.tail(1))
        
        #st.write(data[data['ID']==id])
        data_new = data_copy[data_copy['ID']==id]
        data_new.drop(columns=['ID', 'ICU'],inplace=True)
        k = data_copy.index[data_copy['ID']==id].tolist()
        k=k[0]
        
        
        filename= "my_model2.pkl"
        model = pickle.load(open(filename,'rb'))
                
        #st.write(data_new.head(10))
        X_test=data_copy.drop(columns=['ID','ICU'])
        ICU = model.predict(data_new)
        explainer = shap.Explainer(model)
        shap_values=explainer(X_test)
        print("K add: ",k)
        st.write("Patient added")
        #st.write(data_copy.tail(1))
        st.write(f"My prediction is {ICU}")
        st.write('---')
        st.write("SHAP Value")
        st_shap(shap.plots.waterfall(shap_values[k]),400)
        st_shap(shap.plots.force(shap_values[k],link="logit"),400)
        st_shap(shap.plots.force(shap_values[k]),400)
        expected=explainer.expected_value
        st_shap(shap.decision_plot(expected,shap_values[k].values,X_test),400)
        
        
        data_copy.loc[data_copy["ID"]==id,'ICU']=ICU
        st.write(data_copy.tail(1))
        data=data_copy
        
        
    return data
    #return data
        
    
     
    
    
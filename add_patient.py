import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb
def enter_new_data(data):
    d={}
    for col in data.columns:
        d[col]=0
    id= st.number_input("Enter id of new patient",format="%d",step=1)
    d["Unnamed: 0"]=id
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
    data=data.drop(columns=['ICU'])
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
    st.write(data.head(1))
        
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
    print(len(d))
    #st.write(data.head(10))
    if st.button("Add patient and predict"):
        filename="my_model2.pkl"
        model = pickle.load(open(filename,'rb'))
       
        #data.loc[len(data.index)]=list(map(lambda x: 0, data.columns))
        #st.write(data[-1])
        data=data.append(d,ignore_index=True)
        st.write(data.tail(1))
        
        #st.write(data[data['Unnamed: 0']==id])
        data_new = data[data['Unnamed: 0']==id]
        data_new.drop(columns=['Unnamed: 0', 'ICU'],inplace=True)
        
        
        print("1")
        filename= "my_model2.pkl"
        model = pickle.load(open(filename,'rb'))
        print("2")        
        
        ICU = model.predict(data_new)
        
        print("3")
        st.write(f"My prediction is {ICU}")
        data[data["Unnamed: 0"]==id]['ICU']=ICU
        data.to_csv("/stage_1_balanced.csv",sep=";")
        
        #for opt in multisel:
            #data.loc[len(data.index),[opt]]=1
        
    return data
        
    
     
    
    
from __future__ import division
import pandas as pd
import numpy as np
import os.path
from sklearn.externals import joblib

def load_data():

    inputData = pd.read_csv('inputData.csv').set_index('patientID')

    covariates = data.get([
                           'definitiveRT', 'male', 'age', 'hypopharynx/larynx', 'oropharynx/oral cavity',
                           'nasopharynx/nasal cavity', 'unknown primary', 'parotid',
                           'indChemo', 'noConChemo', 'cisplatin', 'carboplatin', 'cisCarbo',
                           'V020', 'V040', 'V060', 'V080', 'V100', 'V120', 'V140', 'V160',
                           'V180', 'V200', 'V220', 'V240', 'V260'
                            ])
    
    return covariates

def load_ntcp_model():
    
    ntcpModel = joblib.load('Model/mucositisacuteOMrandomForestClassification.pkl')

    return ntcpModel

def predict_ntcp(covariates, ntcpModel):

    ntcpPredictions = ntcpModel.predict_proba(covariates)[:, 1]

    return ntcpPredictions

loadData = load_data()
ntcpModel = load_ntcp_model()
predictNtcp = predict_ntcp(covariates, ntcpModel)

np.set_printoptions(precision = 2)
print 'NTCP = ', predictNtcp
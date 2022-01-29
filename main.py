# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020

@author: win10
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Borrowers import Borrower
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()


proba_pickle = 'proba_model.sav'
proba_model = pickle.load(open(proba_pickle, 'rb'))

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Add /docs to the link above to be directed to Swagger'}


@app.post('/predictUnpaid')
def predict_unpaid(data:Borrower):
    data = data.dict()
    PAYMENT_RATE=data['PAYMENT_RATE']
    AMT_ANNUITY=data['AMT_ANNUITY']
    DAYS_BIRTH=data['DAYS_BIRTH']
    DAYS_EMPLOYED=data['DAYS_EMPLOYED']
    ANNUITY_INCOME_PERC=data['ANNUITY_INCOME_PERC']
    prediction = proba_model.predict_proba([[PAYMENT_RATE,AMT_ANNUITY,DAYS_BIRTH,DAYS_EMPLOYED,ANNUITY_INCOME_PERC]])
    
    return {
        'prediction': str( round(prediction[0][1], 2))
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000/docs
# if __name__ == '__main__':
    # uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn main:app --reload
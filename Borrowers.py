# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Borrower(BaseModel):
    PAYMENT_RATE: float 
    AMT_ANNUITY: float 
    DAYS_BIRTH: float 
    DAYS_EMPLOYED: float
    ANNUITY_INCOME_PERC: float
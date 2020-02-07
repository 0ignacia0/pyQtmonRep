#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:53:54 2020

@author: rguerra
"""


import pandas as pd
import entry
import pyQt_monRep as pyGUI
import cli
import log

# col0:date col1:duration col2:activity col3:group col4:title col5:desc col6:paycode
def lg2df(lgObj):     
    data = []
    for i in range(len(lgObj.entryArray)):
        data.append(lgObj.entryArray[i].getAll())
    tempDf = pd.DataFrame(data)
    entryDf = tempDf.transpose()
    return entryDf

import os.path
import pickle
import warnings
import pandas as pd
from excelhandler import *
from database import *
from sharedOperationsVillar import saveTolerances

#If you want to save a key to a path
#saveExcelDataLocation(key="VillarBearingData")



#loadData(path="Data/saveData.p",expose=True)
#If you want to load data to variable db #
db = loadExcelDataLocation(expose=True)


#Loads an excel from file path location in db[key]
workbook = readExcel(db["VillarBearingData"])


saveTolerances(workbook, longname='Data/BearingData/BearingData1.p', shortname='Data/BearingData/BearingData2.p')






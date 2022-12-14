import pandas as pd
import easygui
from Packages.database import *

def readExcel(fileLocation):

    try:
        workbook = pd.read_excel(fileLocation)
    except:
        print("Location Error")
    return workbook

def saveExcelDataLocation(key = None,variable = None):

    if variable == None:
        variable = easygui.fileopenbox("Please chose Respective Bearing Data")
    if key == None:
        key = input("Please define Database identifier key   ")

    saveData(key=key, variable = variable)
    print("Save Data Complete")

def loadExcelDataLocation(key = None, expose = False, path ='Packages/Data/saveData.p'):

    if key == None:
        db = loadData(path, expose)
    else:
        db = loadData(path, expose)
        db = db[key]
    return db


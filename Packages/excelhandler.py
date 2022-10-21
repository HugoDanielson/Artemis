import pandas as pd
import easygui
from Packages.database import *

def readExcel(fileLocation):

    try:
        workbook = pd.read_excel(fileLocation)
    except:
        print("Location Eerror")
    return workbook


def saveExcelDataLocation(key = None,variable = None):

    if variable == None:
        variable = easygui.fileopenbox("Please chose Respective Bearing Data")
    if key == None:
        key = input("Please define Database identifier key   ")

    saveData(key=key, variable = variable)
    print("Save Data Complete")

def loadExcelDataLocation(key = None, expose = False):

    if key == None:
        db = loadData('Packages/Data/saveData.p', expose)
    else:
        db = loadData('Packages/Data/saveData.p', expose)
        db = db[key]
    return db


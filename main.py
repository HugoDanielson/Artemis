import os.path
import pickle
import warnings
import pandas as pd
from Packages.excelhandler import *
from Packages.database import *
from Packages.sharedOperationsVillar import saveTolerances

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    db = loadExcelDataLocation(expose=True)

    # Loads an excel from file path location in db[key]
    workbook = readExcel(db["VillarBearingData"])

    saveTolerances(workbook, longname='Data/BearingData/BearingData1.p', shortname='Data/BearingData/BearingData2.p')

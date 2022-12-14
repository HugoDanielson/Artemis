from Packages.DataScript import *
from Packages.excelhandler import *
from Packages.sharedOperationsVillar import *
import pandas as pd


from Packages.sharedOperationsVillar import saveTolerances

# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    db = loadExcelDataLocation(expose=True)

    # Loads an excel from file path location in db[key]
    workbook = readExcel(db["VillarBearingData"])

    saveTolerances(workbook, longname='Packages/Data/BearingData/Villar/BearingData2.p', shortname='Packages/Data/BearingData/Villar/BearingData1.p')
    #saveTolerances(pd.read_excel('C:/Users/ag1156/Documents/Artemis/Database/Villar/SUPBDATA.xlsx'))


    #saveExcelDataLocation(key="VillarBearingData")
    #path = "Packages/Data/BearingData/Villar/"

    run_script()

    #wb = excelLoader(db["AerospaceTemplate"])
    #excelFiller(wb, name="VillarFile", path="Packages/Data/BearingData/Villar/")

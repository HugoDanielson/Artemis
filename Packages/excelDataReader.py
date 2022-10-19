import os.path
import pickle
import warnings
import pandas as pd
import easygui
from database import savedata, loadData


key = "VillarBearingData"
variable = easygui.fileopenbox("Please chose Respective Bearing Data")

#if you want to save data
savedata(key, variable)

#If you want to load data#
loadData('Data/saveData.p','true')




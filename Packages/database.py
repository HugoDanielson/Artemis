
import pickle


def loadData(path = 'Data/saveData.p',expose = "false"):
    # loadData(path = 'Data/saveData.p',expose = "true")
    #if you want to enable print set expose = "true"
    expose = expose.lower()

    dbfile = open(path, 'rb')
    db = pickle.load(dbfile)
    if expose == "true":
        for keys in db:
            print('database size =', len(db))
            print(keys, '=>', db[keys])

    dbfile.close()



def savedata(key,variable, path = 'Data/saveData.p'):
    #Function to save a new variable in SaveData.
    #saveData (key,variable,database = {})
    #Key is the unique identifier in the dictionary. Important when you want to retrieve later.
    #Variable is the appended variable that you want saved.
    #Database is the database to be used.
    # For example in the event you want to save the path of where the Excel file to be retrieved is; , Key = Path, Variable is the directory "Data/saveData,p", database = db


    # stringify
    db = {}
    if variable == None or key == None:
        print("No Variable or Key")
        quit(101)

    if key == type(str):
        key = key
    else:
        key = str(key)


   # Obj = {'key': key, 'variable' : variable}


    try:
        db[key] = variable
    except:
        print("Warning db error")

    try:
        dbfile = open(path, 'wb')
        # source, destination
        pickle.dump(db, dbfile)
        dbfile.close()
    except:
        print("Warning dbfile error")
        dbfile.close()

import pickle


def loadData(path = None,expose = False):
    # loadData(path = 'Data/saveData.p',expose = "true")
    #if you want to enable print set expose = "true"
    if path == None:
        quit(1111)

    dbfile = open(path, 'rb')
    db = pickle.load(dbfile)
    if expose == True:
        print(db)

    dbfile.close()
    return db

def save(data, path,rewrite=True):

    if rewrite == True:

        try:
            dbfile = open(path, 'wb')
            pickle.dump(data, dbfile)
            dbfile.close()
        except:
            print("Warning dbfile error")
            dbfile.close()
    elif rewrite == False:
        dbfile = open(path, 'rb')
        db = pickle.load(data,dbfile)
        dbfile.close()

        dbfile = open(path, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()

def saveData (key=None,variable=None, path = "Packages/Data/saveData.p"):

    #Function to save a new variable in SaveData.
    #saveData (key,variable,database = {})
    #Key is the unique identifier in the dictionary. Important when you want to retrieve later.
    #Variable is the appended variable that you want saved.
    #Database is the database to be used.
    # For example in the event you want to save the path of where the Excel file to be retrieved is; , Key = Path, Variable is the directory "Data/saveData,p", database = db
    # stringify
    try:
        dbfile = open(path, 'rb')
        db = pickle.load(dbfile)
        dbfile.close()
    except:
        db = {}

    if variable == None:
        print("No Variable defined")
        quit(101)
    elif key != None:
        key = str(key)
        db[key] = variable


    try:
        dbfile = open(path, 'wb')
        pickle.dump(db, dbfile)
        dbfile.close()
    except:
        print("Warning dbfile error")
        dbfile.close()


import pymongo

class DatabaseConnector:

    def __init__(self) -> None:
        self.uri = "mongodb://wfmandalorian:4UaMpDeWZo1fmTb0tpTmZ2XKTEuBpiWLOdME9jhYhm1Zw2jjULTbzNvnDOWAkkC7Z2UMQz0edawGeekXZkcLjg==@wfmandalorian.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@wfmandalorian@"
        self.dbName = "pronounce-tool"
    
    def getConnection(self):
        return pymongo.MongoClient(self.uri)


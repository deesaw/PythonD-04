import sqlite3
class dbOperations():
    connection=None
    def __init__(self):
        pass
    def connectToDB(self,dbName='taskdb.db'):
        connection = sqlite3.connect(dbName)
        cursor = connection.cursor()
        return connection
    def getCursor(self,connection):
        cursor = connection.cursor()
        return cursor
    def executeQuery(self,cursor,sql):
        return cursor.execute(sql)
    def closeConnection(self,connection):
        connection.close
    def selectQuery(self,connection,tableName):
        pass
    

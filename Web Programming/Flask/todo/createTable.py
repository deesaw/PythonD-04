import sqlite3
conn = sqlite3.connect("taskdb.db")#connecting to a database
cursor = conn.cursor()
# create a table
sql="""CREATE TABLE mytask
                  (tid INTEGER PRIMARY KEY AUTOINCREMENT,task text,done BOOLEAN DEFAULT {}) 
               """.format(False)
cursor.execute(sql)
print("Table Created")
for row in cursor.execute("SELECT * FROM mytask"):
    print (row)
print("after")

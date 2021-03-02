#insert values in to the database
import sqlite3
conn = sqlite3.connect("taskdb.db")
cursor = conn.cursor()
### insert some data
##cursor.execute("INSERT INTO mytask VALUES ('AMAR')")
##for row in cursor.execute("SELECT * FROM task"):
##    print (row)
### save data to database
##sql="delete from tasks where new_task='(AMAR)'"
##cursor.execute(sql)
for row in cursor.execute("SELECT * FROM mytask"):
    print (row)
print('*************')
#print(cursor.execute('DESC mytask'))
conn.commit()

print("Records Inserted")
conn.close()

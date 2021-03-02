import sqlite3 as lite
import sys
try:
    con = lite.connect('mydatabase.db')
    cur = con.cursor()  
    cur.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars VALUES(1,'Audi',52642);
        INSERT INTO Cars VALUES(2,'Mercedes',57127);
        INSERT INTO Cars VALUES(3,'Skoda',9000);
        INSERT INTO Cars VALUES(4,'Volvo',29000);
        INSERT INTO Cars VALUES(5,'Bentley',350000);
        INSERT INTO Cars VALUES(6,'Citroen',21000);
        INSERT INTO Cars VALUES(7,'Hummer',41400);
        INSERT INTO Cars VALUES(8,'Volkswagen',21600);
        """)
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()

    for row in rows:
        print( row )

    con.commit()
    
except lite.Error as e:
    
    if con:
        con.rollback()
        
    print ("Error {}:" .format(e.args[0]))
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 

import sqlite3

def createtable():
    connect = sqlite3.connect("collection.db")
    cur=connect.cursor()
    cur.execute("Create table if NOT EXISTS store (Name STRING, Age INTEGER, Language CHAR)")
    connect.commit()
    connect.close()

def insertdata():
    connect = sqlite3.connect("collection.db")
    cur= connect.cursor()
    cur.execute("Insert INTO store VALUES('Amit', '25', 'E')")
    cur.execute("Insert INTO store VALUES('Shweta', '25' , 'M')")
    connect.commit()
    connect.close()

def viewdata():
    connect = sqlite3.connect(("collection.db"))
    cur = connect.cursor()
    cur.execute(("Select * from store"))
    rows = cur.fetchall()
    connect.close()
    return rows

print (viewdata())
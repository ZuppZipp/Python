import MySQLdb

def insertdb():
    connect = MySQLdb.connect(host = "localhost",
                          user = "root",
                          passwd = "chahal",
                          db = "play")
    cur = connect.cursor()
    cur.execute("Insert INTO data VALUES('Amit','M','2017-12-07')")
    connect.commit()
    connect.close()

def fetchpara(input):
    try:
        conect = MySQLdb.connect(host="localhost", user="root", passwd="chahal", db="play")n
        cur = connect.cursor()
        cur.execute("select * from data where name = '%s'" % input)
        data = cur.fetchone()
        print (data)
        if data is None:
            return_code = "Not Found"
        else:
            return_code = "Found"
        connect.close()
    except MySQLdb.OperationalError:
        return_code = "Database Connection Error"
    return return_code

print (fetchpara("Amit"))

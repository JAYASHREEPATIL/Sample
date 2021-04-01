import mysql.connector


def insert_data(uname,pswd):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="root", database="projectdb")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO login(name, number) VALUES ("{0}","{1}");'.format(uname, pswd)
    dbcursor.execute(sql)
    mysqldb.commit()
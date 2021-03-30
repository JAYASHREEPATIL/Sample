import mysql.connector


def insert_data(name, number):
    mysqldb = mysql.connector.connect(host="127.0.0.1", user="root",
                                      passwd="password", database="rasa_feedback")
    dbcursor = mysqldb.cursor()
    sql = 'INSERT INTO test1 (name, number) VALUES ("{0}","{1}");'.format(name, number)
    dbcursor.execute(sql)
    mysqldb.commit()



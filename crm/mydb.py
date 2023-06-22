import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0445450232aA'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE proshtor")

print('All done!')

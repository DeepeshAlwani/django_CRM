import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Deepesh@1234',
)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE dev")

print("All Done!")
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root@mysql'

	)

# Preparing a cursor object
cursorObject = dataBase.cursor()

# Creating a database
cursorObject.execute("CREATE DATABASE rickSugar")

print("All Done!")
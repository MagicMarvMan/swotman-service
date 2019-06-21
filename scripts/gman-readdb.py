import mysql.connector
import os

mydb = mysql.connector.connect(
  host=os.environ.get("DB_HOST"),
  user=os.environ.get("DB_USER"),
  passwd=os.environ.get("DB_PASSWD"),
  database=os.environ.get("DB_DATABASE")
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM govdomains")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
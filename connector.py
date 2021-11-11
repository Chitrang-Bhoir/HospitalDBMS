import mysql.connector

#connect to database
hospital_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Suchita@1123",
  database="hospital"
)

#define a cursor
c = hospital_db.cursor()
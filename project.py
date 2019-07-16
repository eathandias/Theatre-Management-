import mysql.connector as pvp
mydb=pvp.connect(host="localhost",user="root",password="Eathan234")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE movies")

#This code works, also im testing how collabrative correction
#takes place

import sqlite3
# connecting to the database
connection = sqlite3.connect("programs/research.db")
crsr = connection.cursor()
#sql_command = """"""
#crsr.execute(sql_command)
#print("Connected to the database")
#connection.close()

loginCreds = input('Enter Access Key:\n')
f = open('programs/access.key')
AccessKey = f.read()
if loginCreds == AccessKey:
    menu1 = input('A)dd Research\nD)elete Research\nE)dit Research\n')
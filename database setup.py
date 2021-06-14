import mysql.connector as MySQLdb
t=str(input("Enter My SQL Password: "))
db = MySQLdb.connect(host="localhost",user="root",passwd=t)
cur = db.cursor()

#Creating Database
cur.execute("create database hotel_management_system")
db.commit()

#Switching to database
db = MySQLdb.connect(host="localhost",user="root",passwd=t, database="hotel_management_system")

#Creating Members table
cur.execute("create table members(membership_id char(5) Primary Key, First_name varchar(20) not null, Last_name varchar(20) not null, phone_no char(13) not null unique, Email_ID varchar(35) not null, Points integer default(0))")
db.commit()
#Creating Rooms Table
db.commit()


print("Setup was successful")

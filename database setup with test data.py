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
# Test data For Members
cur.execute("insert into members values ('X0001','Nick','Paper',9999912318,'nick@gmail.com',100), ('X0002','Joe','Wick',9876543210,'joe@gmail.com',100), ('X0003','Mark','Pitcher',7654321890,'mark@gmail.com',100), ('X0004','Luzi','Parker',9587412512,'luzi@gmail.com',100), ('X0005','Jim','Windows',8746230624,'jim@gmail.com',100), ('X0006','Rodger','Jobs',5471862789,'rodger@gmail.com',200), ('X0007','Josh','Zacher',6947152870,'josh@gmail.com',200), ('X0008','Henry','Ashley',4375217890,'henry@gmail.com',200), ('X0009','William','Hams',1247896321,'william@gmail.com',200), ('X0010','James','Cobler',2458791350,'james@gmail.com',300)")
db.commit()

#Creating Rooms Table
db.commit()
#Data for Rooms
db.commit()


print("Setup was successful and test data has been added!")

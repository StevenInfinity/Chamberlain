import mysql.connector as MySQLdb
from time import sleep
from sys import exit
t=str(input("Enter MySQL Password: "))

def tp(text):
    for character in text:
        sleep(0.1)
        print(character, end='', flush=True)
    print()

try:
    db = MySQLdb.connect(host="localhost",user="root",passwd=t)
except:
    tp("\nConnection Failed...\nClosing...\n")
    exit()

db = MySQLdb.connect(host="localhost",user="root",passwd=t)
cur = db.cursor()

tp("\n-- Successfully Connected to Server --\n")
def create_memtbl():
    #Creating Members table
    cur.execute("create table members(membership_id integer(5) Primary Key, First_name varchar(20) not null, Last_name varchar(20) not null, phone_no char(13) not null unique, Email_ID varchar(35) not null, Points integer default 0);")
    db.commit()
    tp("\nMembers' table created...")
    # Test data For Members
    cur.execute("insert into members values (10001,'Nick','Paper',9999912318,'nick@gmail.com',100), (10002,'Joe','Wick',9876543210,'joe@gmail.com',100), (10003,'Mark','Pitcher',7654321890,'mark@gmail.com',100), (10004,'Luzi','Parker',9587412512,'luzi@gmail.com',100), (10005,'Jim','Windows',8746230624,'jim@gmail.com',100), (10006,'Rodger','Jobs',5471862789,'rodger@gmail.com',200), (10007,'Josh','Zacher',6947152870,'josh@gmail.com',200), (10008,'Henry','Ashley',4375217890,'henry@gmail.com',200), (10009,'William','Hams',1247896321,'william@gmail.com',200), (10010,'James','Cobler',2458791350,'james@gmail.com',300);")
    db.commit()
    tp("10 test records inserted to Members' table...")
    
def create_roomstbl():
    #Creating Rooms Table
    cur.execute("create table rooms(Room_no char(3) Primary Key,Fee_per_day integer default 1000,Occupancy enum('Occupied','Vacant'),membership_id integer(5) ,Check_in_date date );")
    db.commit()
    tp("\nRooms table created...")
    # Test data For Rooms
    cur.execute("insert into rooms(Room_no,Fee_per_day,Occupancy,membership_id,check_in_date) values ('100',5000,'Occupied',10001,'2021-01-01'), ('101',5000,'Occupied',10002,'2021-02-01'), ('102',7000,'Occupied',10003,'2021-03-01'), ('103',6000,'Occupied',10004,'2021-04-01'), ('104',7000,'Occupied',10005,'2021-05-01'), ('105',6000,'Occupied',10006,'2021-06-01'), ('106',5000,'Occupied',10007,'2021-07-01'), ('107',6000,'Occupied',10008,'2021-08-01'), ('108',7000,'Vacant',NULL,NULL), ('109',6000,'Vacant' ,NULL, NULL);")
    db.commit()
    tp("10 test records inserted to Rooms' table...")

def create_billstbl():
    #Creating Bills Table
    cur.execute("CREATE TABLE Bills(Bill_no integer(5) ZEROFILL, Room_no char(3), Mem_ID integer(5),Days integer, Amount integer, PRIMARY KEY (Bill_no), FOREIGN KEY (Room_no) REFERENCES Rooms(Room_no), FOREIGN KEY (Mem_ID) REFERENCES Members(Membership_ID));")
    print("\nBill's table created...")
    #Test Data For Bills
    print("Query Incomplete for insertion of data to bills table")

def create_db():
    #Creating Database
    cur.execute("create database hotel_management_system")
    db.commit()
    tp("\nDatabase created...")
    cur.execute("use hotel_management_system")

cur.execute("Show databases")
a=cur.fetchall()
if ('hotel_management_system',) in a:
    tp("\nDatabase already exists...")
    cur.execute("Use hotel_management_system")
    cur.execute("show tables")
    b=cur.fetchall()
    if ('members',) in b:
        tp("\nMembers' Table already exists...")
    else:
        create_memtbl()
    if ('rooms',) in b:
        tp("\nRooms Table already exists...")
    else:
        create_roomstbl()
    if ('bills',) in b:
        tp("\nBills Table already exists...")
    else:
        create_billstbl()
else:
    create_db()
    create_memtbl()
    create_roomstbl()
    create_billstbl()
tp("\n-- Setup was Successful --\n")
#Cleaning Environment
db.close()

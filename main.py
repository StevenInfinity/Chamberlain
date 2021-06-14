from tkinter import *
import mysql.connector as mysql
import threading
from tabulate import tabulate
from tkinter import ttk

# __________________________________

# Functions

# Quit Function and Window____________________________________________
def esc_window():
    exit_page = Toplevel()
    exit_page.geometry("325x310")
    exit_page.resizable(0, 0)
    Label(exit_page, text="", bg='#2D2926').grid(row=1)
    exit_page.title("Quit Window")
    exit_page.configure(bg="#2D2926")
    Label(exit_page, text=" ╔══════════╗", bg='#2D2926',font="Corbel 18 bold", fg="red").grid(row=2)
    Label(exit_page, text=" Are you sure you want to quit?",bg="#2D2926", fg="red", font="Corbel 14 bold").grid(row=3)
    Label(exit_page, text=" ╚══════════╝", bg="#2D2926",font="Corbel 18 bold", fg="red").grid(row=4)
    Label(exit_page, text="", bg="#2D2926").grid(row=5)
    yes_button = Button(exit_page, text="YES", fg="red2", font="Corbel 10 bold",width=20, height=2, bd=10, command=quit).grid(row=6)
    Label(exit_page, text="", bg="#2D2926").grid(row=7)
    no_button = Button(exit_page, text="NO", fg="green3", font="Corbel 10 bold",width=20, height=2, bd=10, command=exit_page.destroy).grid(row=8)

# MEMBERS WINDOW's ALL WINDOWS AND FUNCTION_________________________

# Adding Member record command and window
def add_member():
    t="All fields are mandatory"
    def add_member_info():
        v1=id_var.get()
        v2=first_var.get()
        v3=last_var.get()
        v4=phone_number_var.get()
        v5=email_var.get()
        if v1 and v2 and v3 and v4 and v5!=None:
            sql="insert into members values ('%s','%s','%s','%s','%s',0)"%(v1,v2,v3,v4,v5)
            cur.execute(sql)
            db.commit()
            id_var.set("")
            first_var.set("")
            last_var.set("")
            phone_number_var.set("")
            email_var.set("")
        else:
            t="One or more field(s) are empty"
    def clear_cmd():
        id_var.set("")
        first_var.set("")
        last_var.set("")
        phone_number_var.set("")
        email_var.set("")
    add_member_window = Toplevel()
    add_member_window.title("Add Member")
    add_member_window.geometry("400x600")
    add_member_window.resizable(0, 0)
    add_member_window.configure(bg="#101820")
    #Title
    Label(add_member_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(add_member_window, text="  Add Member",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(add_member_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(add_member_window, text="", bg="#101820").grid(row=4)
    #Entry declaration
    id_var=StringVar()
    first_var=StringVar()
    last_var=StringVar()
    phone_number_var=StringVar()
    email_var=StringVar()
    #Error Notice
    Label(add_member_window, text=t, bg="#101820",fg="#F2AA4C").grid(row=5)#DETAILS ERROR
    Label(add_member_window, text="", bg="#101820").grid(row=6)
    #Membership ID Entry
    Label(add_member_window, text="    Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(pady=10,row=7, sticky="w")
    ID_entry = (Entry(add_member_window, width=15, font="Corbel 14",textvariable=id_var).grid(pady=10,row=7, sticky="e"))
    #First Name Entry
    Label(add_member_window, text="    Enter First Name :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(pady=10,row=8, sticky="w")
    first_name_entry = (Entry(add_member_window, width=15, font="Corbel 14",textvariable=first_var).grid(pady=10,row=8, sticky="e"))
    #Last Name Entry
    Label(add_member_window, text="    Enter Last Name :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(pady=10,row=9, sticky="w")
    last_name_entry = (Entry(add_member_window, width=15, font="Corbel 14",textvariable=last_var).grid(pady=10,row=9, sticky="e"))
    #Phone Number Entry
    Label(add_member_window, text="    Enter Phone Number :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(pady=10,row=10, sticky="w")
    phone_number_entry = (Entry(add_member_window, width=15, font="Corbel 14",textvariable=phone_number_var).grid(pady=10,row=10, sticky="e"))
    #Email ID Entry
    Label(add_member_window, text="    Enter Email ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(pady=11,row=11, sticky="w")
    email_entry = (Entry(add_member_window, width=15, font="Corbel 14",textvariable=email_var).grid(pady=10,row=11, sticky="e"))
    #Buttons
    Button(add_member_window, text="Add Member", font="Corbel 10", width=20,height=2, bd=5, command=add_member_info).grid(padx=25,pady=15,row=12,sticky="w")
    Button(add_member_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=add_member_window.destroy).grid(padx=15,pady=15,row=13)
    Button(add_member_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(padx=15,pady=15,row=12,sticky="e")
    

# Displaying all members record
def all_members():
    all_members_window = Toplevel()
    all_members_window.title("All Members Details")
    all_members_window.geometry("945x500")
    all_members_window.resizable(0, 0)
    all_members_window.configure(bg="#101820")
    cur.execute("SELECT * FROM members")
    myresult = cur.fetchall()
    main_frame = Frame(all_members_window, bg="#101820")
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame, bg="#101820")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(bg="#101820", yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas, bg="#101820")
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    Label(second_frame, text=" ╔══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C", padx=25).grid(row=1,column=1)
    Label(second_frame, text="Members", bg="#101820", fg="#F2AA4C",font="Corbel 20 bold", padx=100).grid(row=2,column=1)
    Label(second_frame, text=" ╚══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3,column=1)
    Label(second_frame, text="", bg="#101820").grid(row=4)
    details = Label(second_frame, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(pady=10, padx=20, row=5, column=1)
    Label(second_frame, text="", bg="#101820").grid(row=6)
    Button(second_frame, text="Close Window", font="Corbel 10", width=20, height=2,bd=5, command=all_members_window.destroy).grid(row=7, column=1, sticky="s")


#SEARCH FUNCTION_____________________________________
# Searching members by Membership ID
def search_by_ID():
    def search_id():
        search_result=Toplevel()
        search_result.title("Search Result")
        search_result.geometry("935x320")
        search_result.resizable(0, 0)
        search_result.configure(bg="#101820")
        Label(search_result, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(search_result, text="  Result",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(search_result, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(search_result, text="", bg="#101820").grid(row=4)
        #Data
        m_id=id_var.get()
        sql="select * from members WHERE Membership_ID = '%s'" % m_id
        cur.execute(sql)
        myresult = cur.fetchall()
        #Showing Result
        result = Label(search_result, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(padx=20,row=5)
        Label(search_result, text="", bg="#101820").grid(row=6)
        Button(search_result,text="Close Window",font="Corbel 10",width=20,height=2,bd=5,command=search_result.destroy).grid(row=7)                                                                                                                 
        
    def clear_cmd():
        id_var.set("")

    id_var=StringVar()
    
    search_by_ID_window = Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by ID")
    search_by_ID_window.configure(bg="#101820")
    Label(search_by_ID_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(search_by_ID_window, text="  Search By Membership ID",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(search_by_ID_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(search_by_ID_window, text="", bg="#101820").grid(row=4)
    Label(search_by_ID_window, text="    Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    ID_entry = (Entry(search_by_ID_window, width=15, font="Consolas 14",textvariable=id_var).grid(row=5, sticky="e"))
    #
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(search_by_ID_window, text="Search", font="Corbel 10", width=20, height=2,bd=5, command=search_id).grid(row=7, sticky="w", padx=30, pady=20)
    Button(search_by_ID_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(search_by_ID_window, text=" ", bg="#101820").grid(row=8)
    Button(search_by_ID_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=search_by_ID_window.destroy).grid(row=9)
    Label(search_by_ID_window, text="Membership ID is 10 characters long and is unique to each member",bg="#101820", fg="#F2AA4C", font="Corbel 8").grid(row=10, sticky="sw", pady=20)


def search_by_phone_number():
    def search_phone_number():
        search_result=Toplevel()
        search_result.title("Search Result")
        search_result.geometry("935x320")
        search_result.resizable(0, 0)
        search_result.configure(bg="#101820")
        Label(search_result, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(search_result, text="  Result",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(search_result, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(search_result, text="", bg="#101820").grid(row=4)
        #Data
        phone_number=phone_number_var.get()
        sql="select * from members WHERE Phone_no = '%s'" % phone_number
        cur.execute(sql)
        myresult = cur.fetchall()
        #Showing Result
        result = Label(search_result, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(padx=20,row=5)
        Label(search_result, text="", bg="#101820").grid(row=6)
        Button(search_result,text="Close Window",font="Corbel 10",width=20,height=2,bd=5,command=search_result.destroy).grid(row=7)                                                                                                                 
        
    def clear_cmd():
        phone_number_var.set("")

    phone_number_var=StringVar()
    
    search_by_ID_window = Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Phone Number")
    search_by_ID_window.configure(bg="#101820")
    Label(search_by_ID_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(search_by_ID_window, text="  Search By Phone Number",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(search_by_ID_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(search_by_ID_window, text="", bg="#101820").grid(row=4)
    Label(search_by_ID_window, text="    Enter Phone Number :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    phone_number_entry = (Entry(search_by_ID_window, width=15, font="Consolas 14",textvariable=phone_number_var).grid(row=5, sticky="e"))
    #
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(search_by_ID_window, text="Search", font="Corbel 10", width=20, height=2,bd=5, command=search_phone_number).grid(row=7, sticky="w", padx=30, pady=20)
    Button(search_by_ID_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(search_by_ID_window, text=" ", bg="#101820").grid(row=8)
    Button(search_by_ID_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=search_by_ID_window.destroy).grid(row=9)
    
def search_by_email():
    def search_email():
        search_result=Toplevel()
        search_result.title("Search Result")
        search_result.geometry("935x320")
        search_result.resizable(0, 0)
        search_result.configure(bg="#101820")
        Label(search_result, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(search_result, text="  Result",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(search_result, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(search_result, text="", bg="#101820").grid(row=4)
        #Data
        email=email_var.get()
        sql="select * from members WHERE Email_ID = '%s'" % email
        cur.execute(sql)
        myresult = cur.fetchall()
        #Showing Result
        result = Label(search_result, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(padx=20,row=5)
        Label(search_result, text="", bg="#101820").grid(row=6)
        Button(search_result,text="Close Window",font="Corbel 10",width=20,height=2,bd=5,command=search_result.destroy).grid(row=7)                                                                                                                 
        
    def clear_cmd():
        email_var.set("")

    email_var=StringVar()
    
    search_by_ID_window = Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Email ID")
    search_by_ID_window.configure(bg="#101820")
    Label(search_by_ID_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(search_by_ID_window, text="  Search By Email ID",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(search_by_ID_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(search_by_ID_window, text="", bg="#101820").grid(row=4)
    Label(search_by_ID_window, text="    Enter Email ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    email_entry = (Entry(search_by_ID_window, width=15, font="Consolas 14",textvariable=email_var).grid(row=5, sticky="e"))
    #
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(search_by_ID_window, text="Search", font="Corbel 10", width=20, height=2,bd=5, command=search_email).grid(row=7, sticky="w", padx=30, pady=20)
    Button(search_by_ID_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(search_by_ID_window, text=" ", bg="#101820").grid(row=8)
    Button(search_by_ID_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=search_by_ID_window.destroy).grid(row=9)

    
#Searching by First Name and Last Name
def search_by_name():
    def search_phone_number():
        search_result=Toplevel()
        search_result.title("Search Result")
        search_result.geometry("935x320")
        search_result.resizable(0, 0)
        search_result.configure(bg="#101820")
        Label(search_result, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(search_result, text="  Result",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(search_result, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(search_result, text="", bg="#101820").grid(row=4)
        #Data
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        sql="select * from members WHERE first_name = '%s' and last_name='%s'" % (first_name, last_name)
        cur.execute(sql)
        myresult = cur.fetchall()
        #Showing Result
        result = Label(search_result, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(padx=20,row=5)
        Label(search_result, text="", bg="#101820").grid(row=6)
        Button(search_result,text="Close Window",font="Corbel 10",width=20,height=2,bd=5,command=search_result.destroy).grid(row=7)                                                                                                                 
        
    def clear_cmd():
        first_name_var.set("")
        last_name_var.set("")

    first_name_var=StringVar()
    last_name_var=StringVar()
    
    search_by_ID_window = Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Name")
    search_by_ID_window.configure(bg="#101820")
    Label(search_by_ID_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(search_by_ID_window, text="  Search By Name",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(search_by_ID_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(search_by_ID_window, text="", bg="#101820").grid(row=4)
    Label(search_by_ID_window, text="    Enter First Name :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    first_name_entry = (Entry(search_by_ID_window, width=15, font="Consolas 14",textvariable=first_name_var).grid(row=5, sticky="e"))
    Label(search_by_ID_window, text="    Enter Last Name :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=6, sticky="w")
    last_name_entry = (Entry(search_by_ID_window, width=15, font="Consolas 14",textvariable=last_name_var).grid(row=6, sticky="e"))
    #
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(search_by_ID_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(search_by_ID_window, text="Search", font="Corbel 10", width=20, height=2,bd=5, command=search_phone_number).grid(row=7, sticky="w", padx=30, pady=20)
    Button(search_by_ID_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(search_by_ID_window, text=" ", bg="#101820").grid(row=8)
    Button(search_by_ID_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=search_by_ID_window.destroy).grid(row=9)

    

# Displaying Members record Options
def display_members_options():
    display_members_window = Toplevel()
    display_members_window.geometry("400x550")
    display_members_window.resizable(0, 0)
    display_members_window.title("Members Details Options")
    display_members_window.configure(bg="#101820")
    Label(display_members_window, text=" ╔══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C", padx=20).grid(row=1)
    Label(display_members_window, text="Search Members", bg="#101820",fg="#F2AA4C", font="Corbel 20 bold", padx=90).grid(row=2)
    Label(display_members_window, text=" ╚══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(display_members_window, text="", bg="#101820").grid(row=4)
    Button(display_members_window, text="All Members", width=20,height=2, command=all_members, bd=5).grid(row=5)
    Label(display_members_window, text="", bg="#101820").grid(row=6)
    Button(display_members_window, text="Search By ID", width=20,height=2, command=search_by_ID, bd=5).grid(row=7)
    Label(display_members_window, text="", bg="#101820").grid(row=8)
    Button(display_members_window, text="Search By Phone Number", width=20,height=2, command=search_by_phone_number, bd=5).grid(row=9)
    Label(display_members_window, text="", bg="#101820").grid(row=10)
    Button(display_members_window, text="Search By Email ID", width=20,height=2, command=search_by_email, bd=5).grid(row=11)
    Label(display_members_window, text="", bg="#101820").grid(row=12)
    Button(display_members_window, text="Search By Name", width=20,height=2, command=search_by_name, bd=5).grid(row=13)
    Label(display_members_window, text="", bg="#101820").grid(row=14)
    Button(display_members_window, text="Close Window", width=20,height=2, command=display_members_window.destroy, bd=5).grid(row=15)

#END OF SEARCH FUNCTIONS_______________________________________


#DELETE FUNCTIONS______________________________________________
#Delete all members
def delete_all_members():
    def delete_all():
        def close_windows():
            delete_result.destroy()
            delete_all_window.destroy()
        delete_result=Toplevel()
        delete_result.title("Delete Confirmation")
        delete_result.geometry("300x300")
        sql="delete from members"
        cur.execute(sql) 
        delete_result.resizable(0, 0)
        delete_result.configure(bg="#101820")
        Label(delete_result, text="", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(delete_result, text="  All Record Deleted",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(delete_result, text="", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Button(delete_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=close_windows).grid(row=4)
        db.commit()   

    delete_all_window = Toplevel()
    delete_all_window.geometry("400x200")
    delete_all_window.resizable(0, 0)
    delete_all_window.title("Delete All Member")
    delete_all_window.configure(bg="#101820")
    Label(delete_all_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(delete_all_window, text="  Delete All Members",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(delete_all_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Button(delete_all_window, text="Yes", font="Corbel 10", width=20, height=2,bd=5, command=delete_all).grid(row=4, sticky="w", padx=30, pady=20)
    Button(delete_all_window, text="No", font="Corbel 10", width=20,height=2, bd=5, command=delete_all_window.destroy).grid(row=4, sticky="e", pady=20)

    

#Delete member by ID
def delete_by_ID():
    def delete_id():
        delete_result=Toplevel()
        delete_result.title("Delete Confirmation")
        delete_result.geometry("300x200")
        membership_id=membership_id_var.get()
        sql="delete from members WHERE membership_id = '%s'" % membership_id
        cur.execute(sql) 
        delete_result.resizable(0, 0)
        delete_result.configure(bg="#101820")
        Label(delete_result, text="", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(delete_result, text="  Record Deleted",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(delete_result, text="", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Button(delete_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_result.destroy).grid(row=4)
        db.commit()   
    def clear_cmd():
        membership_id_var.set("")

    membership_id_var=StringVar()
    
    delete_by_id_window = Toplevel()
    delete_by_id_window.geometry("400x400")
    delete_by_id_window.resizable(0, 0)
    delete_by_id_window.title("Delete Member by Email ID")
    delete_by_id_window.configure(bg="#101820")
    Label(delete_by_id_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(delete_by_id_window, text="  Delete By Membership ID",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(delete_by_id_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(delete_by_id_window, text="", bg="#101820").grid(row=4)
    Label(delete_by_id_window, text="    Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    id_entry = (Entry(delete_by_id_window, width=15, font="Consolas 14",textvariable=membership_id_var).grid(row=5, sticky="e"))
    #
    Label(delete_by_id_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(delete_by_id_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(delete_by_id_window, text="Delete", font="Corbel 10", width=20, height=2,bd=5, command=delete_id).grid(row=7, sticky="w", padx=30, pady=20)
    Button(delete_by_id_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(delete_by_id_window, text=" ", bg="#101820").grid(row=8)
    Button(delete_by_id_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_by_id_window.destroy).grid(row=9)

    

#Delete member by Phone Number
def delete_by_phone_number():
    def delete_phone_number():
        delete_result=Toplevel()
        delete_result.title("Delete Confirmation")
        delete_result.geometry("300x200")
        phone_number=phone_number_var.get()
        sql="delete from members WHERE phone_no = '%s'" % phone_number
        cur.execute(sql) 
        delete_result.resizable(0, 0)
        delete_result.configure(bg="#101820")
        Label(delete_result, text="", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(delete_result, text="  Record Deleted",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(delete_result, text="", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Button(delete_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_result.destroy).grid(row=4)
        db.commit()
    def clear_cmd():
        phone_number_var.set("")

    phone_number_var=StringVar()
    
    delete_by_phone_number_window = Toplevel()
    delete_by_phone_number_window.geometry("400x400")
    delete_by_phone_number_window.resizable(0, 0)
    delete_by_phone_number_window.title("Delete Member by Email ID")
    delete_by_phone_number_window.configure(bg="#101820")
    Label(delete_by_phone_number_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(delete_by_phone_number_window, text="  Delete By Phone Number",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(delete_by_phone_number_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(delete_by_phone_number_window, text="", bg="#101820").grid(row=4)
    Label(delete_by_phone_number_window, text="    Enter Phone Number :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    email_entry = (Entry(delete_by_phone_number_window, width=15, font="Consolas 14",textvariable=phone_number_var).grid(row=5, sticky="e"))
    #
    Label(delete_by_phone_number_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(delete_by_phone_number_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(delete_by_phone_number_window, text="Delete", font="Corbel 10", width=20, height=2,bd=5, command=delete_phone_number).grid(row=7, sticky="w", padx=30, pady=20)
    Button(delete_by_phone_number_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(delete_by_phone_number_window, text=" ", bg="#101820").grid(row=8)
    Button(delete_by_phone_number_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_by_phone_number_window.destroy).grid(row=9)


    

#Delete member by Email ID
def delete_by_email():
    def delete_email():
        delete_result=Toplevel()
        delete_result.title("Delete Confirmation")
        delete_result.geometry("300x200")
        delete_result.resizable(0, 0)
        delete_result.configure(bg="#101820")
        Label(delete_result, text="", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(delete_result, text="  Record Deleted",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(delete_result, text="", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Button(delete_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_result.destroy).grid(row=4)
        #Data
        email=email_var.get()
        sql="delete from members WHERE Email_ID = '%s'" % email
        cur.execute(sql)                                                                                                          
        db.commit()
    def clear_cmd():
        email_var.set("")

    email_var=StringVar()
    
    delete_by_email_window = Toplevel()
    delete_by_email_window.geometry("400x400")
    delete_by_email_window.resizable(0, 0)
    delete_by_email_window.title("Delete Member by Email ID")
    delete_by_email_window.configure(bg="#101820")
    Label(delete_by_email_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(delete_by_email_window, text="  Delete By Email ID",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(delete_by_email_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(delete_by_email_window, text="", bg="#101820").grid(row=4)
    Label(delete_by_email_window, text="    Enter Email ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    #
    email_entry = (Entry(delete_by_email_window, width=15, font="Consolas 14",textvariable=email_var).grid(row=5, sticky="e"))
    #
    Label(delete_by_email_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=6)
    Label(delete_by_email_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(delete_by_email_window, text="Delete", font="Corbel 10", width=20, height=2,bd=5, command=delete_email).grid(row=7, sticky="w", padx=30, pady=20)
    Button(delete_by_email_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(delete_by_email_window, text=" ", bg="#101820").grid(row=8)
    Button(delete_by_email_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=delete_by_email_window.destroy).grid(row=9)

    
#DELETE OPTIONS
def delete_member_options():
    delete_member_options_window=Toplevel()
    delete_member_options_window.geometry("400x475")
    delete_member_options_window.resizable(0, 0)
    delete_member_options_window.title("Delete Member Options")
    delete_member_options_window.configure(bg="#101820")
    Label(delete_member_options_window, text=" ╔══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C", padx=20).grid(row=1)
    Label(delete_member_options_window, text="Delete Member", bg="#101820",fg="#F2AA4C", font="Corbel 20 bold", padx=90).grid(row=2)
    Label(delete_member_options_window, text=" ╚══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(delete_member_options_window, text="", bg="#101820").grid(row=4)
    Button(delete_member_options_window, text="Delete All Members", width=20,height=2, command=delete_all_members, bd=5).grid(row=5)
    Label(delete_member_options_window, text="", bg="#101820").grid(row=6)
    Button(delete_member_options_window, text="Delete By ID", width=20,height=2, command=delete_by_ID, bd=5).grid(row=7)
    Label(delete_member_options_window, text="", bg="#101820").grid(row=8)
    Button(delete_member_options_window, text="Delete By Phone Number", width=20,height=2, command=delete_by_phone_number, bd=5).grid(row=9)
    Label(delete_member_options_window, text="", bg="#101820").grid(row=10)
    Button(delete_member_options_window, text="Delete By Email ID", width=20,height=2, command=delete_by_email, bd=5).grid(row=11)
    Label(delete_member_options_window, text="", bg="#101820").grid(row=12)
    Button(delete_member_options_window, text="Close Window", width=20,height=2, command=delete_member_options_window.destroy, bd=5).grid(row=13)
    
#END OF DELETE FUNCTIONS__________________________________


#UPDATE FUNCTIONS_________________________________________
#Update Phone Number
def update_phone_number_window():
    def update_phone_number():
        update_result=Toplevel()
        update_result.title("Confirmation")
        update_result.geometry("350x200")
        update_result.resizable(0, 0)
        update_result.configure(bg="#101820")
        Label(update_result, text="   ╔═════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(update_result, text="  Updated!",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(update_result, text="   ╚═════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(update_result, text="", bg="#101820").grid(row=4)
        #SQL Execution
        mem_id = mem_id_var.get()
        new_phone_number = new_phone_number_var.get()
        sql="update members set phone_no = '%s' WHERE membership_id = '%s'" % (new_phone_number, mem_id)
        cur.execute(sql)
        db.commit()
        def close_windows():
            update_result.destroy()
            update_phone_number_window.destroy()
        Button(update_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=close_windows).grid(row=5)
    def clear_cmd():
        mem_id_var.set("")
        new_phone_number_var.set("")
    #Entry String declaration
    mem_id_var=StringVar()
    new_phone_number_var=StringVar()
    #Window
    update_phone_number_window = Toplevel()
    update_phone_number_window.geometry("400x300")
    update_phone_number_window.resizable(0, 0)
    update_phone_number_window.title("Update Phone Number")
    update_phone_number_window.configure(bg="#101820")
    Label(update_phone_number_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(update_phone_number_window, text="  Update Phone Number",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(update_phone_number_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(update_phone_number_window, text="", bg="#101820").grid(row=4)
    Label(update_phone_number_window, text="Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    mem_id_entry = (Entry(update_phone_number_window, width=15, font="Consolas 14",textvariable=mem_id_var).grid(row=5, sticky="e"))
    Label(update_phone_number_window, text="Enter New Phone Number :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=6, sticky="w")
    last_name_entry = (Entry(update_phone_number_window, width=15, font="Consolas 14",textvariable=new_phone_number_var).grid(row=6, sticky="e"))
    Label(update_phone_number_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(update_phone_number_window, text="Update", font="Corbel 10", width=20, height=2,bd=5, command=update_phone_number).grid(row=7, sticky="w", padx=30, pady=20)
    Button(update_phone_number_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(update_phone_number_window, text=" ", bg="#101820").grid(row=8)
    Button(update_phone_number_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=update_phone_number_window.destroy).grid(row=9)

    


#Update Email ID
def update_email_window():
    def update_email_id():
        update_result=Toplevel()
        update_result.title("Confirmation")
        update_result.geometry("350x200")
        update_result.resizable(0, 0)
        update_result.configure(bg="#101820")
        Label(update_result, text="   ╔═════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(update_result, text="  Updated!",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(update_result, text="   ╚═════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(update_result, text="", bg="#101820").grid(row=4)
        #SQL Execution
        mem_id = mem_id_var.get()
        email_id = email_id_var.get()
        sql="update members set email_ID = '%s' WHERE membership_id = '%s'" % (email_id, mem_id)
        cur.execute(sql)
        db.commit()
        def close_windows():
            update_result.destroy()
            update_email_id_window.destroy()
        Button(update_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=close_windows).grid(row=5)
    def clear_cmd():
        mem_id_var.set("")
        email_id_var.set("")
    #Entry String declaration
    mem_id_var=StringVar()
    email_id_var=StringVar()
    #Window
    update_email_id_window = Toplevel()
    update_email_id_window.geometry("400x300")
    update_email_id_window.resizable(0, 0)
    update_email_id_window.title("Update Email ID")
    update_email_id_window.configure(bg="#101820")
    Label(update_email_id_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(update_email_id_window, text="  Update Email ID",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(update_email_id_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(update_email_id_window, text="", bg="#101820").grid(row=4)
    Label(update_email_id_window, text="Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    mem_id_entry = (Entry(update_email_id_window, width=15, font="Consolas 14",textvariable=mem_id_var).grid(row=5, sticky="e"))
    Label(update_email_id_window, text="Enter New Email ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=6, sticky="w")
    email_id_entry = (Entry(update_email_id_window, width=15, font="Consolas 14",textvariable=email_id_var).grid(row=6, sticky="e"))
    Label(update_email_id_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(update_email_id_window, text="Update", font="Corbel 10", width=20, height=2,bd=5, command=update_email_id).grid(row=7, sticky="w", padx=30, pady=20)
    Button(update_email_id_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(update_email_id_window, text=" ", bg="#101820").grid(row=8)
    Button(update_email_id_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=update_email_id_window.destroy).grid(row=9)

    


#Update Points
def update_points_window():
    def update_email_id():
        update_result=Toplevel()
        update_result.title("Confirmation")
        update_result.geometry("350x200")
        update_result.resizable(0, 0)
        update_result.configure(bg="#101820")
        Label(update_result, text="   ╔═════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
        Label(update_result, text="  Updated!",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
        Label(update_result, text="   ╚═════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
        Label(update_result, text="", bg="#101820").grid(row=4)
        #SQL Execution
        mem_id = mem_id_var.get()
        cur.execute("select points from members where membership_id='%s'" % mem_id)
        myresult = cur.fetchall()
        cur_points=myresult[0][0]
        points_add=int(points_add_var.get())
        new_points = cur_points+points_add
        sql="update members set points = '%s' WHERE membership_id = '%s'" % (new_points, mem_id)
        cur.execute(sql)
        db.commit()
        def close_windows():
            update_result.destroy()
            update_points_window.destroy()
        Button(update_result, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=close_windows).grid(row=5)
    def clear_cmd():
        mem_id_var.set("")
        points_add_var.set("")
    #Entry String declaration
    mem_id_var=StringVar()
    points_add_var=StringVar()
    #Window
    update_points_window = Toplevel()
    update_points_window.geometry("400x400")
    update_points_window.resizable(0, 0)
    update_points_window.title("Update Points")
    update_points_window.configure(bg="#101820")
    Label(update_points_window, text="   ╔═══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C").grid(row=1)
    Label(update_points_window, text="  Update Points",bg="#101820", fg="#F2AA4C", font="Corbel 20 bold").grid(row=2)
    Label(update_points_window, text="   ╚═══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(update_points_window, text="", bg="#101820").grid(row=4)
    Label(update_points_window, text="Enter Membership ID :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=5, sticky="w")
    mem_id_entry = (Entry(update_points_window, width=15, font="Consolas 14",textvariable=mem_id_var).grid(row=5, sticky="e"))
    Label(update_points_window, text="Enter Points :", bg="#101820",font="Corbel 14 bold", fg="#F2AA4C").grid(row=6, sticky="w")
    points_add_entry = (Entry(update_points_window, width=15, font="Consolas 14",textvariable=points_add_var).grid(row=6, sticky="e"))
    Label(update_points_window, text=" ", bg="#101820", font="Corbel 20 bold").grid(row=7)
    Button(update_points_window, text="Update", font="Corbel 10", width=20, height=2,bd=5, command=update_email_id).grid(row=7, sticky="w", padx=30, pady=20)
    Button(update_points_window, text="Clear", font="Corbel 10", width=20,height=2, bd=5, command=clear_cmd).grid(row=7, sticky="e", pady=20)
    Label(update_points_window, text=" ", bg="#101820").grid(row=8)
    Button(update_points_window, text="Close Window", font="Corbel 10", width=20,height=2, bd=5, command=update_points_window.destroy).grid(row=9)
    Label(update_points_window, text=" ", bg="#101820").grid(row=10)
    Label(update_points_window, text="Use (-) sign to deduct points ", bg='#101820',font="Corbel 10", fg="#F2AA4C").grid(row=11,sticky="sw")
#Update options window
def update_member_options():
    update_member_options_window = Toplevel()
    update_member_options_window.geometry("400x410")
    update_member_options_window.resizable(0, 0)
    update_member_options_window.title("Update Member Info")
    update_member_options_window.configure(bg="#101820")
    Label(update_member_options_window, text=" ╔══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C", padx=20).grid(row=1)
    Label(update_member_options_window, text="Update Member Info", bg="#101820",fg="#F2AA4C", font="Corbel 20 bold", padx=90).grid(row=2)
    Label(update_member_options_window, text=" ╚══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(update_member_options_window, text="", bg="#101820").grid(row=4)
    Button(update_member_options_window, text="Update Phone Number", width=20,height=2, command=update_phone_number_window, bd=5).grid(row=5)
    Label(update_member_options_window, text="", bg="#101820").grid(row=6)
    Button(update_member_options_window, text="Update Email ID", width=20,height=2, command=update_email_window, bd=5).grid(row=7)
    Label(update_member_options_window, text="", bg="#101820").grid(row=8)
    Button(update_member_options_window, text="Update Points", width=20,height=2, command=update_points_window, bd=5).grid(row=9)
    Label(update_member_options_window, text="", bg="#101820").grid(row=10)
    Button(update_member_options_window, text="Close Window", width=20,height=2, command=update_member_options_window.destroy, bd=5).grid(row=11)

#END OF UPDATE FUNCTIONS__________________________________


# Members Window
def members_window():
    def refresh():
        members_page.destroy()
        members_window()
    members_page = Toplevel()
    members_page.geometry("945x500")
    #members_page.resizable(0, 0)
    members_page.title("Members Window")
    members_page.configure(bg="#101820")
    # Displaying all members' records
    cur.execute("SELECT * FROM members")
    myresult = cur.fetchall()
    main_frame = Frame(members_page, bg="#101820")
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame, bg="#101820")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(bg="#101820")  # , yscrollcommand=my_scrollbar.set)
    #my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas, bg="#101820")
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    second_frame.pack(side=TOP)
    Label(second_frame, text=" ╔══════════╗", bg='#101820',font="Corbel 20 bold", fg="#F2AA4C", padx=25).grid(row=1)
    Label(second_frame, text="Members", bg="#101820", fg="#F2AA4C",font="Corbel 20 bold", padx=100).grid(row=2)
    Label(second_frame, text=" ╚══════════╝", bg="#101820",font="Corbel 20 bold", fg="#F2AA4C").grid(row=3)
    Label(second_frame, text="", bg="#101820").grid(row=4)
    #Refresh Button
    Button(second_frame, text=" Refresh ⟳", width=15,height=2,command=refresh).grid(row=2,sticky="e")
    
    sb = Scrollbar(second_frame).grid(column=1)
    details = Label(second_frame, text=tabulate(myresult, headers=['Membership ID', 'First Name', 'Last Name', 'Phone Number','Email ID', 'Points'], tablefmt='psql'), bg="#101820", fg="#F2AA4C", font="Consolas 12 ").grid(padx=15, row=5)
    Label(second_frame, text="", bg="#101820").grid(row=6)
    # Buttons
    button_frame = Frame(my_canvas, bg="#101820")
    my_canvas.create_window((0, 0), window=button_frame, anchor="sw")
    button_frame.pack(side=BOTTOM)
    Button(button_frame, text="Search Member", width=20, height=2,command=display_members_options, bd=5).grid(row=0, column=0, padx=10, pady=15)
    Button(button_frame, text="Add Member", width=20, height=2,command=add_member, bd=5).grid(row=0, column=1, padx=10)
    Button(button_frame, text="Delete Member", width=20, height=2, command=delete_member_options, bd=5).grid(row=0, column=2, padx=10)
    Button(button_frame, text="Update Member", width=20, height=2, command=update_member_options, bd=5).grid(row=0, column=3, padx=10)
    Button(button_frame, text="Close Window", font="Corbel 10", width=20, height=2,bd=5, command=members_page.destroy).grid(row=0, column=4, padx=10)
#_________________________________________________________


# ROOMS' WINDOWS AND FUNCTIONS____________________________
# Rooms List Window

def rooms_window():
    rooms_page = Toplevel()
    rooms_page.geometry("400x400")
    rooms_page.title("Rooms Info")
    rooms_page.resizable(0, 0)
    rooms_page.configure(bg="#2C5F2D")
    Label(rooms_page, text=" ╔══════════╗", bg='#2C5F2D',font="Corbel 20 bold", fg="#FFE77A", padx=25).grid(row=1)
    Label(rooms_page, text="Room Details", bg="#2C5F2D",fg="#FFE77A", font="Corbel 20 bold").grid(row=2)
    Label(rooms_page, text=" ╚══════════╝", bg="#2C5F2D",font="Corbel 20 bold", fg="#FFE77A").grid(row=3)

# Employees List Window


def employees_window():
    employees_page = Toplevel()
    employees_page.geometry("400x400")
    employees_page.title("Employee Info")
    employees_page.resizable(0, 0)
    employees_page.configure(bg="#606060")
    Label(employees_page, text=" ╔══════════╗", bg='#606060',font="Corbel 20 bold", fg="#D6ED17", padx=25).grid(row=1)
    Label(employees_page, text="Employee Details", bg="#606060",fg="#D6ED17", font="Corbel 20 bold").grid(row=2)
    Label(employees_page, text=" ╚══════════╝", bg='#606060',font="Corbel 20 bold", fg="#D6ED17", padx=25).grid(row=3)


# __________________________________

# Main Window
bg_main = "#00203F"  # "#00539C"
fg_main = "#ADEFD1"  # "#FFD662"
main_window = Tk()
main_window.title("Hotel Management System - Main Menu")
main_window.geometry("400x430")
main_window.resizable(0, 0)
main_window.configure(bg=bg_main)
# HEADING
Label(main_window, text="   Hotel Management System", bg=bg_main,fg=fg_main, font="Corbel 20 bold", pady=25).grid(row=1)
Label(main_window, text="   »»—————　★　—————«« ", bg=bg_main,fg=fg_main, font="Corbel 20 bold").grid(row=2)
# Members list button
Label(main_window, text="", bg=bg_main).grid(row=3)
Button(main_window, text="Members Info", width=20, height=2,command=members_window, bd=5).grid(row=4, column=0)
# Rooms Info button
Label(main_window, text="", bg=bg_main).grid(row=5)
Button(main_window, text="Rooms Info", width=20, height=2,bd=5, command=rooms_window).grid(row=6, column=0)
# Employees Info button
Label(main_window, text="", bg=bg_main).grid(row=7)
Button(main_window, text="Employees Info", width=20, height=2,bd=5, command=employees_window).grid(row=8, column=0)
# Quit Button
Label(main_window, text="", bg=bg_main).grid(row=9)
Button(main_window, text="QUIT", width=20, height=2, bd=5,fg="red2", command=esc_window).grid(row=10, column=0)

# __________________________________
# Database startup
db = mysql.connect(host="localhost", user="root", passwd="12345",database="hotel_management_system")
cur = db.cursor()


threading.Thread(target=main_window.mainloop)




from tkinter import *
from mysql.connector import Error
import mysql.connector as mysql
import threading
from tabulate import tabulate
from tkinter import ttk
from tkinter import messagebox

# __________________________________
#Colors
mem_bg = "#101820"
mem_fg  =  "#F2AA4C"        
main_bg  =  "#303030"   
main_fg  =  "#E8EAF6"           
rooms_bg  =  "#06373A"
rooms_fg  =  "#F2AA4C"
bills_bg  =  "#606060"      
bills_fg  =  "#D6ED17"          
# Functions

# Quit Function and Window____________________________________________
def esc_window():
    def close_app():
        db.close()
        quit()
    exit_page  =  Toplevel()
    exit_page.geometry("325x310")
    exit_page.resizable(0, 0)
    Label(exit_page, text = "", bg = '#2D2926').grid(row = 1)
    exit_page.title("Quit Window")
    exit_page.configure(bg = "#2D2926")
    Label(exit_page, text = " ╔══════════╗", bg = '#2D2926',font = "Corbel 18 bold", fg = "red").grid(row = 2)
    Label(exit_page, text = " Are you sure you want to quit?",bg = "#2D2926", fg = "red", font = "Corbel 14 bold").grid(row = 3)
    Label(exit_page, text = " ╚══════════╝", bg = "#2D2926",font = "Corbel 18 bold", fg = "red").grid(row = 4)
    Label(exit_page, text = "", bg = "#2D2926").grid(row = 5)
    yes_button  =  Button(exit_page, text = "YES", fg = "red2", font = "Corbel 10 bold",width = 20, height = 2, bd = 10, command = close_app).grid(row = 6)
    Label(exit_page, text = "", bg = "#2D2926").grid(row = 7)
    no_button  =  Button(exit_page, text = "NO", fg = "green3", font = "Corbel 10 bold",width = 20, height = 2, bd = 10, command = exit_page.destroy).grid(row = 8)

# MEMBERS WINDOW's ALL WINDOWS AND FUNCTION_________________________

# Adding Member record command and window
def add_member():
    t = "All fields are mandatory"
    def add_member_info():
        cur.execute("select max(membership_id) from members")
        temp = cur.fetchall()
        temp = temp[0][0]
        if temp == None:
            temp=10000
        temp_new_id = temp+1
        v1 = temp_new_id
        v2 = first_var.get()
        v3 = last_var.get()
        v4 = phone_number_var.get()
        v5 = email_var.get()
        if v1 and v2 and v3 and v4 and v5!= "":
            sql = "insert into members values (%s,'%s','%s','%s','%s',0)" % (v1,v2,v3,v4,v5)
            cur.execute(sql)
            db.commit()
            #id_var.set("")
            first_var.set("")
            last_var.set("")
            phone_number_var.set("")
            email_var.set("")
            messagebox.showinfo("Member","New Member added with ID %s"%v1 ,parent = add_member_window)
            add_member_window.destroy()
        else:
            messagebox.showerror("Add Member","One or more field(s) are empty" ,parent = add_member_window)
    def clear_cmd():
        first_var.set("")
        last_var.set("")
        phone_number_var.set("")
        email_var.set("")
    add_member_window  =  Toplevel()
    add_member_window.title("Add Member")
    add_member_window.geometry("400x550")
    add_member_window.resizable(0, 0)
    add_member_window.configure(bg = mem_bg)
    #Title
    Label(add_member_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(add_member_window, text = "  Add Member",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(add_member_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(add_member_window, text = "", bg = mem_bg).grid(row = 4)
    #Entry declaration
    first_var = StringVar()
    last_var = StringVar()
    phone_number_var = StringVar()
    email_var = StringVar()
    #Error Notice
    Label(add_member_window, text = t, bg = mem_bg,fg = mem_fg).grid(row = 5)#DETAILS ERROR
    Label(add_member_window, text = "", bg = mem_bg).grid(row = 6)
    #First Name Entry
    Label(add_member_window, text = "    Enter First Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 8, sticky = "w")
    first_name_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = first_var).grid(pady = 10,row = 8, sticky = "e"))
    #Last Name Entry
    Label(add_member_window, text = "    Enter Last Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 9, sticky = "w")
    last_name_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = last_var).grid(pady = 10,row = 9, sticky = "e"))
    #Phone Number Entry
    Label(add_member_window, text = "    Enter Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 10, sticky = "w")
    phone_number_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = phone_number_var).grid(pady = 10,row = 10, sticky = "e"))
    #Email ID Entry
    Label(add_member_window, text = "    Enter Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 11,row = 11, sticky = "w")
    email_entry  =  (Entry(add_member_window, width = 15, font = "Consolas 14",textvariable = email_var).grid(pady = 10,row = 11, sticky = "e"))
    #Buttons
    Button(add_member_window, text = "Add Member", font = "Corbel 10", width = 20,height = 2, bd = 5, command = add_member_info).grid(padx = 25,pady = 15,row = 12,sticky = "w")
    Button(add_member_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = add_member_window.destroy).grid(padx = 15,pady = 15,row = 13)
    Button(add_member_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(padx = 15,pady = 15,row = 12,sticky = "e")
    

# Displaying all members record
def all_members():
    all_members_window  =  Toplevel()
    all_members_window.title("All Members Details")
    all_members_window.geometry("700x475")
    all_members_window.resizable(0, 0)
    all_members_window.configure(bg = mem_bg)
    cur.execute("SELECT * FROM members")
    myresult  =  cur.fetchall()
    Label(all_members_window, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(all_members_window, text = "Members", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(all_members_window, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    #Setting the Table
    tree  =  ttk.Treeview(all_members_window, column = ("c1", "c2", "c3","c4","c5","c6"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Mem. ID")
    tree.column("#2", anchor = CENTER,width = 130)
    tree.heading("#2", text = "First Name")
    tree.column("#3", anchor = CENTER,width = 130)
    tree.heading("#3", text = "Last Name")
    tree.column("#4", anchor = CENTER,width = 100)
    tree.heading("#4", text = "Ph. No.")
    tree.column("#5", anchor = CENTER,width = 130)
    tree.heading("#5", text = "Email ID")
    tree.column("#6", anchor = CENTER,width = 100)
    tree.heading("#6", text = "Points")
    tree.pack(pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row) 
    #Close Button
    Button(all_members_window, text = "Close Window", font = "Corbel 10", width = 20, height = 2,bd = 5, command = all_members_window.destroy).pack(side = BOTTOM,pady = 10)


#SEARCH FUNCTION_____________________________________
# Searching members by Membership ID
def search_by_ID():
    def search_id():
        m_id = id_var.get()
        try:
            m_id = int(m_id)
            sql = "select * from members WHERE Membership_ID  =  %s" % m_id
            cur.execute(sql)
            myresult  =  cur.fetchall()
            if myresult !=[]:
                search_result = Toplevel()
                search_result.title("Search Result")
                search_result.geometry("935x320")
                search_result.resizable(0, 0)
                search_result.configure(bg = mem_bg)
                Label(search_result, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
                Label(search_result, text = "  Result",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
                Label(search_result, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
                Label(search_result, text = "", bg = mem_bg).grid(row = 4)
                #Showing Result
                result  =  Label(search_result, text = tabulate(myresult, headers = ['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt = 'fancy_grid'), bg = mem_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
                Label(search_result, text = "", bg = mem_bg).grid(row = 6)
                Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
            else:
                messagebox.showinfo("Search Member","No member found with membership ID %s" % m_id ,parent = search_by_ID_window)
        except:
            messagebox.showerror("Search Member","Invalid Membership ID entered" ,parent = search_by_ID_window)
    def clear_cmd():
        id_var.set("")
    id_var = StringVar()
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by ID")
    search_by_ID_window.configure(bg = mem_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Membership ID",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = mem_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter Membership ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    #
    ID_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = id_var).grid(row = 5, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_id).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)
    Label(search_by_ID_window, text = "Membership ID is 5 characters long and is unique to each member",bg = mem_bg, fg = mem_fg, font = "Corbel 8").grid(row = 10, sticky = "sw", pady = 20)


def search_by_phone_number():
    def search_phone_number():
        #Data
        phone_number = phone_number_var.get()
        sql = "select * from members WHERE Phone_no  =  '%s'" % phone_number
        cur.execute(sql)
        myresult  =  cur.fetchall()
        if myresult != []:
            #Window
            search_result = Toplevel()
            search_result.title("Search Result")
            search_result.geometry("935x320")
            search_result.resizable(0, 0)
            search_result.configure(bg = mem_bg)
            Label(search_result, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
            Label(search_result, text = "  Result",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
            Label(search_result, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
            Label(search_result, text = "", bg = mem_bg).grid(row = 4)
            #Showing Result
            result  =  Label(search_result, text = tabulate(myresult, headers = ['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt = 'fancy_grid'), bg = mem_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
            Label(search_result, text = "", bg = mem_bg).grid(row = 6)
            Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
        else:
            messagebox.showinfo("Search Member","No member found with Phone Number %s" % phone_number ,parent = search_by_ID_window)
    def clear_cmd():
        phone_number_var.set("")

    phone_number_var = StringVar()
    
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Phone Number")
    search_by_ID_window.configure(bg = mem_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Phone Number",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = mem_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    #
    phone_number_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = phone_number_var).grid(row = 5, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_phone_number).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)
    
def search_by_email():
    def search_email():
        #Data
        email = email_var.get()
        sql = "select * from members WHERE Email_ID  =  '%s'" % email
        cur.execute(sql)
        myresult  =  cur.fetchall()
        if myresult != []:
            search_result = Toplevel()
            search_result.title("Search Result")
            search_result.geometry("935x320")
            search_result.resizable(0, 0)
            search_result.configure(bg = mem_bg)
            Label(search_result, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
            Label(search_result, text = "  Result",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
            Label(search_result, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
            Label(search_result, text = "", bg = mem_bg).grid(row = 4)
            #Showing Result
            result  =  Label(search_result, text = tabulate(myresult, headers = ['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt = 'fancy_grid'), bg = mem_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
            Label(search_result, text = "", bg = mem_bg).grid(row = 6)
            Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
        else:
            messagebox.showinfo("Search Member","No member found with Email ID %s" % email, parent = search_by_ID_window)
    def clear_cmd():
        email_var.set("")

    email_var = StringVar()
    
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Email ID")
    search_by_ID_window.configure(bg = mem_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Email ID",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = mem_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    #
    email_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = email_var).grid(row = 5, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_email).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)

    
#Searching by First Name and Last Name
def search_by_name():
    def search_name():
         #Data
        first_name = first_name_var.get()
        last_name = last_name_var.get()
        sql = "select * from members WHERE first_name  =  '%s' and last_name = '%s'" % (first_name, last_name)
        cur.execute(sql)
        myresult  =  cur.fetchall()
        if myresult != []:
            search_result = Toplevel()
            search_result.title("Search Result")
            search_result.geometry("935x320")
            search_result.resizable(0, 0)
            search_result.configure(bg = mem_bg)
            Label(search_result, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
            Label(search_result, text = "  Result",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
            Label(search_result, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
            Label(search_result, text = "", bg = mem_bg).grid(row = 4)
            #Showing Result
            result  =  Label(search_result, text = tabulate(myresult, headers = ['Membership ID', 'First Name', 'Last Name', 'Phone Number', 'Email ID','Points'], tablefmt = 'fancy_grid'), bg = mem_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
            Label(search_result, text = "", bg = mem_bg).grid(row = 6)
            Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
        else:
            messagebox.showinfo("Search Member","No member found with Name %s %s" % (first_name,last_name), parent = search_by_ID_window)
    def clear_cmd():
        first_name_var.set("")
        last_name_var.set("")

    first_name_var = StringVar()
    last_name_var = StringVar()
    
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Member by Name")
    search_by_ID_window.configure(bg = mem_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Name",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = mem_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter First Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    #
    first_name_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = first_name_var).grid(row = 5, sticky = "e"))
    Label(search_by_ID_window, text = "    Enter Last Name :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 6, sticky = "w")
    last_name_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = last_name_var).grid(row = 6, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_name).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)

    

# Search Members record Options
def display_members_options():
    display_members_window  =  Toplevel()
    display_members_window.geometry("400x550")
    display_members_window.resizable(0, 0)
    display_members_window.title("Members Details Options")
    display_members_window.configure(bg = mem_bg)
    Label(display_members_window, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 20).grid(row = 1)
    Label(display_members_window, text = "Search Members", bg = mem_bg,fg = mem_fg, font = "Corbel 20 bold", padx = 90).grid(row = 2)
    Label(display_members_window, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 4)
    Button(display_members_window, text = "All Members", width = 20,height = 2, command = all_members, bd = 5).grid(row = 5)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 6)
    Button(display_members_window, text = "Search By ID", width = 20,height = 2, command = search_by_ID, bd = 5).grid(row = 7)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 8)
    Button(display_members_window, text = "Search By Phone Number", width = 20,height = 2, command = search_by_phone_number, bd = 5).grid(row = 9)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 10)
    Button(display_members_window, text = "Search By Email ID", width = 20,height = 2, command = search_by_email, bd = 5).grid(row = 11)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 12)
    Button(display_members_window, text = "Search By Name", width = 20,height = 2, command = search_by_name, bd = 5).grid(row = 13)
    Label(display_members_window, text = "", bg = mem_bg).grid(row = 14)
    Button(display_members_window, text = "Close Window", width = 20,height = 2, command = display_members_window.destroy, bd = 5).grid(row = 15)

#END OF SEARCH FUNCTIONS_______________________________________


#UPDATE FUNCTIONS_________________________________________
#Update Phone Number
def update_phone_number_window():
    def update_phone_number():
        #SQL Execution
        mem_id  =  mem_id_var.get()
        mem_id = mem_id.strip()
        new_phone_number  =  new_phone_number_var.get()
        new_phone_number = new_phone_number.strip()
        try:
            mem_id = int(mem_id)
            int(new_phone_number)
            cur.execute("select membership_id from members")
            temp_mid_list = cur.fetchall()
            if new_phone_number and mem_id != "":
                if (mem_id,) in temp_mid_list:
                    sql = "update members set phone_no  =  '%s' WHERE membership_id  =  %s" % (new_phone_number, mem_id)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo("Update Member Info","Member Information was updated!", parent = update_phone_number_window)
                    clear_cmd()
                else:
                    messagebox.showerror("Update Member Info","Member with Membership ID %s does not exit" % mem_id, parent = update_phone_number_window)
            else:
                messagebox.showerror("Update Member Info","Enter a valid Membership ID and a a valid Phone Number", parent = update_phone_number_window)
        except:
            messagebox.showerror("Update Member Info","Enter a valid Membership ID and a a valid Phone Number", parent = update_phone_number_window)
    def clear_cmd():
        mem_id_var.set("")
        new_phone_number_var.set("")
    #Entry String declaration
    mem_id_var = StringVar()
    new_phone_number_var = StringVar()
    #Window
    update_phone_number_window  =  Toplevel()
    update_phone_number_window.geometry("400x300")
    update_phone_number_window.resizable(0, 0)
    update_phone_number_window.title("Update Phone Number")
    update_phone_number_window.configure(bg = mem_bg)
    Label(update_phone_number_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(update_phone_number_window, text = "  Update Phone Number",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(update_phone_number_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(update_phone_number_window, text = "", bg = mem_bg).grid(row = 4)
    Label(update_phone_number_window, text = "Enter Membership ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    mem_id_entry  =  (Entry(update_phone_number_window, width = 15, font = "Consolas 14",textvariable = mem_id_var).grid(row = 5, sticky = "e"))
    Label(update_phone_number_window, text = "Enter New Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 6, sticky = "w")
    last_name_entry  =  (Entry(update_phone_number_window, width = 15, font = "Consolas 14",textvariable = new_phone_number_var).grid(row = 6, sticky = "e"))
    Label(update_phone_number_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(update_phone_number_window, text = "Update", font = "Corbel 10", width = 20, height = 2,bd = 5, command = update_phone_number).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(update_phone_number_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(update_phone_number_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(update_phone_number_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = update_phone_number_window.destroy).grid(row = 9)

    
#Update Email ID
def update_email_window():
    def update_email_id():
        cur.execute("select membership_id from members")
        temp_mid_list = cur.fetchall()
        #SQL Execution
        mem_id  =  mem_id_var.get()
        mem_id = mem_id.strip()
        email_id  =  email_id_var.get()
        email_id = email_id.strip()
        try:
            mem_id = int(mem_id)
            if mem_id and email_id != "":
                if (mem_id,) in temp_mid_list:
                    sql = "update members set email_ID  =  '%s' WHERE membership_id  =  %s" % (email_id, mem_id)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo("Update Member Info","Member Information was updated!", parent = update_email_id_window)
                    clear_cmd()
                else:
                    messagebox.showerror("Update Member Info","Member with Membership ID %s does not exist or is invalid" % mem_id, parent = update_email_id_window)

            else:
                messagebox.showerror("Update Member Info","Enter a valid Membership ID and a Valid Email ID", parent = update_email_id_window)
        except:
            messagebox.showerror("Update Member Info","Enter a valid Membership ID and a Valid Email ID", parent = update_email_id_window)
       
    def clear_cmd():
        mem_id_var.set("")
        email_id_var.set("")
    #Entry String declaration
    mem_id_var = StringVar()
    email_id_var = StringVar()
    #Window
    update_email_id_window  =  Toplevel()
    update_email_id_window.geometry("400x300")
    update_email_id_window.resizable(0, 0)
    update_email_id_window.title("Update Email ID")
    update_email_id_window.configure(bg = mem_bg)
    Label(update_email_id_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(update_email_id_window, text = "  Update Email ID",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(update_email_id_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(update_email_id_window, text = "", bg = mem_bg).grid(row = 4)
    Label(update_email_id_window, text = "Enter Membership ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    mem_id_entry  =  (Entry(update_email_id_window, width = 15, font = "Consolas 14",textvariable = mem_id_var).grid(row = 5, sticky = "e"))
    Label(update_email_id_window, text = "Enter New Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 6, sticky = "w")
    email_id_entry  =  (Entry(update_email_id_window, width = 15, font = "Consolas 14",textvariable = email_id_var).grid(row = 6, sticky = "e"))
    Label(update_email_id_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(update_email_id_window, text = "Update", font = "Corbel 10", width = 20, height = 2,bd = 5, command = update_email_id).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(update_email_id_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(update_email_id_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(update_email_id_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = update_email_id_window.destroy).grid(row = 9)

    
#Update Points
def update_points_window():
    def update_email_id():
        cur.execute("select membership_id from members")
        temp_mid_list = cur.fetchall()
        mem_id  =  mem_id_var.get()
        mem_id = mem_id.strip()
        try:
            mem_id = int(mem_id)
            if mem_id != "":
                if (mem_id,) in temp_mid_list:
                    cur.execute("select points from members where membership_id = %s" % mem_id)
                    myresult  =  cur.fetchall()
                    cur_points = myresult[0][0]
                    points_add = int(points_add_var.get())
                    new_points  =  cur_points+points_add
                    sql = "update members set points  =  '%s' WHERE membership_id  =  %s" % (new_points, mem_id)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo("Update Member Info","Member Information was updated!", parent = update_points_window) 
                    clear_cmd()
                else:
                    messagebox.showerror("Update Member Info","Member with Membership ID %s does not exist  or is invalid" % mem_id, parent = update_points_window)  
            else:
                messagebox.showerror("Update Member Info","Enter a valid Membership ID and points", parent = update_points_window)    
        except:
            messagebox.showerror("Update Member Info","Invalid Membership ID or points value", parent = update_points_window)    

    def clear_cmd():
        mem_id_var.set("")
        points_add_var.set("")
    #Entry String declaration
    mem_id_var = StringVar()
    points_add_var = StringVar()
    #Window
    update_points_window  =  Toplevel()
    update_points_window.geometry("400x400")
    update_points_window.resizable(0, 0)
    update_points_window.title("Update Points")
    update_points_window.configure(bg = mem_bg)
    Label(update_points_window, text = "   ╔═══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(update_points_window, text = "  Update Points",bg = mem_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(update_points_window, text = "   ╚═══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(update_points_window, text = "", bg = mem_bg).grid(row = 4)
    Label(update_points_window, text = "Enter Membership ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    mem_id_entry  =  (Entry(update_points_window, width = 15, font = "Consolas 14",textvariable = mem_id_var).grid(row = 5, sticky = "e"))
    Label(update_points_window, text = "Enter Points :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 6, sticky = "w")
    points_add_entry  =  (Entry(update_points_window, width = 15, font = "Consolas 14",textvariable = points_add_var).grid(row = 6, sticky = "e"))
    Label(update_points_window, text = " ", bg = mem_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(update_points_window, text = "Update", font = "Corbel 10", width = 20, height = 2,bd = 5, command = update_email_id).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(update_points_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(update_points_window, text = " ", bg = mem_bg).grid(row = 8)
    Button(update_points_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = update_points_window.destroy).grid(row = 9)
    Label(update_points_window, text = " ", bg = mem_bg).grid(row = 10)
    Label(update_points_window, text = "Use (-) sign to deduct points ", bg = mem_bg,font = "Corbel 10", fg = mem_fg).grid(row = 11,sticky = "sw")


#Update options window
def update_member_options():
    update_member_options_window = Toplevel()
    update_member_options_window.geometry("400x410")
    update_member_options_window.resizable(0, 0)
    update_member_options_window.title("Update Member Info")
    update_member_options_window.configure(bg = mem_bg)
    Label(update_member_options_window, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 20).grid(row = 1)
    Label(update_member_options_window, text = "Update Member Info", bg = mem_bg,fg = mem_fg, font = "Corbel 20 bold", padx = 90).grid(row = 2)
    Label(update_member_options_window, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(update_member_options_window, text = "", bg = mem_bg).grid(row = 4)
    Button(update_member_options_window, text = "Update Phone Number", width = 20,height = 2, command = update_phone_number_window, bd = 5).grid(row = 5)
    Label(update_member_options_window, text = "", bg = mem_bg).grid(row = 6)
    Button(update_member_options_window, text = "Update Email ID", width = 20,height = 2, command = update_email_window, bd = 5).grid(row = 7)
    Label(update_member_options_window, text = "", bg = mem_bg).grid(row = 8)
    Button(update_member_options_window, text = "Update Points", width = 20,height = 2, command = update_points_window, bd = 5).grid(row = 9)
    Label(update_member_options_window, text = "", bg = mem_bg).grid(row = 10)
    Button(update_member_options_window, text = "Close Window", width = 20,height = 2, command = update_member_options_window.destroy, bd = 5).grid(row = 11)

#END OF UPDATE FUNCTIONS__________________________________


# Members Window
def members_window():
    def refresh():
        members_page.destroy()
        members_window()
    members_page  =  Toplevel()
    members_page.geometry("700x500")
    members_page.resizable(0, 0)
    members_page.title("Members Window")
    members_page.configure(bg = mem_bg)
    # Getting all members' records
    cur.execute("SELECT * FROM members")
    myresult  =  cur.fetchall()
    #Label
    Label(members_page, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(members_page, text = "Members", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(members_page, text = " ╚══════════╝", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    #Refresh Button
    Button(members_page, text = " Refresh ⟳", width = 12,height = 1,command = refresh).pack(side = TOP,anchor = "ne",padx = 20)
    #Setting the Table
    tree  =  ttk.Treeview(members_page, column = ("c1", "c2", "c3","c4","c5","c6"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Mem. ID")
    tree.column("#2", anchor = "e",width = 130)
    tree.heading("#2", text = "First Name")
    tree.column("#3", anchor = "w",width = 130)
    tree.heading("#3", text = "Last Name")
    tree.column("#4", anchor = "w",width = 100)
    tree.heading("#4", text = "Ph. No.")
    tree.column("#5", anchor = "w",width = 130)
    tree.heading("#5", text = "Email ID")
    tree.column("#6", anchor = CENTER,width = 100)
    tree.heading("#6", text = "Points")
    tree.pack(expand = YES,pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row)
    
    #Members treeview double click event
    def getSelection(event):
        #Function to update from double click event window
        def doubleClickUpdate():
            mem_id = curitem[0]
            pno = phone_number_var.get()
            emid = email_var.get()
            pts = points_var.get()
            if mem_id and pno and emid != "":
                sql = "UPDATE members SET phone_no = '%s' where membership_id = %s " % (pno,mem_id)
                cur.execute(sql)
                sql = "UPDATE members SET points = %s where membership_id = %s " % (pts,mem_id)
                cur.execute(sql)
                sql = "UPDATE members SET email_id = '%s' where membership_id = %s " % (emid,mem_id)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo("Update Member Details","Details of member with membership ID %s was updated" % mem_id ,parent = datawindow)
            else:
                messagebox.showerror("Update Member Details", "Phone Number and Email ID are mandatory fields, please fill these fields.")
        
        #getSelection(Datawindow) main code
        currow = tree.focus()
        curitem = (tree.item(currow))['values']
        datawindow = Toplevel()
        datawindow.configure(bg = mem_bg)
        datawindow.geometry("400x550")
        datawindow.resizable(0,0)
        datawindow.title("Member details edit Window")
        Label(datawindow, text = " ╔══════════╗", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).grid(row = 1,pady = 10)
        Label(datawindow, text = "Member details", bg = mem_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).grid(row = 2,sticky = 'news')
        Label(datawindow, text = " ╚══════════╝\n", bg = mem_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3, sticky = 'news')
        display_mem = "Membership ID:\t" + str(curitem[0])
        Label(datawindow, text = display_mem, bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 4, sticky = 'nws',padx = 10)
        Label(datawindow, text = "Name of member:\t" + curitem[1] + " " + curitem[2] , bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 5, sticky = 'nws', padx = 10)
        Label(datawindow, text = "" , bg = mem_bg,font = "Consolas 16 bold", fg = mem_fg).grid(row = 6, sticky = 'nws', padx = 10)
    
        phone_number_var = StringVar()
        email_var = StringVar()
        points_var = StringVar()
        #Label and textboxes
        Label(datawindow, text = "Phone Number :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 7, sticky = "w",padx = 10)
        phone_number_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = phone_number_var).grid(pady = 10,row = 7, sticky = "e", padx = 35))
        phone_number_var.set(curitem[3])
        Label(datawindow, text = "Email ID :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 8, sticky = "w",padx = 10)
        email_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = email_var).grid(pady = 10,row = 8, sticky = "e",padx = 35))
        email_var.set(curitem[4])
        Label(datawindow, text = "Points :", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 9, sticky = "w",padx = 10)
        points_entry  =  (Entry(datawindow, width = 20, font = "Consolas 14",textvariable = points_var).grid(pady = 10,row = 9, sticky = "e",padx = 35))
        points_var.set(curitem[5])
        #Buttons
        Label(datawindow, text = "", bg = mem_bg,font = "Corbel 14 bold", fg = mem_fg).grid(pady = 10,row = 10, sticky = "w",padx = 10)
        Button(datawindow, text = "Update", font = "Corbel 10", width = 20,height = 2, bd = 5, command = doubleClickUpdate).grid(padx = 25,pady = 15,row = 11,sticky = "w")
        Button(datawindow, text = "Close", font = "Corbel 10", width = 20,height = 2, bd = 5, command = datawindow.destroy).grid(padx = 15,pady = 15,row = 11,sticky = "e")
    #Binding double click event to function
    tree.bind('<Double-1>', getSelection)
    
    # Buttons
    Button(members_page, text = "Search Member", width = 20, height = 2,command = display_members_options, bd = 5).pack(side = LEFT,padx = 20,pady = 15)
    Button(members_page, text = "Add Member", width = 20, height = 2,command = add_member, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(members_page, text = "Update Member", width = 20, height = 2, command = update_member_options, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(members_page, text = "Close Window", font = "Corbel 10", width = 20, height = 2,bd = 5, command = members_page.destroy).pack(side = LEFT,padx = 10,pady = 15)
#_________________________________________________________


# ROOMS' WINDOWS AND FUNCTIONS____________________________
# Rooms List Window

def display_all_rooms():
    all_rooms_window = Toplevel()
    all_rooms_window.title("Rooms Details")
    all_rooms_window.geometry("700x500")
    all_rooms_window.resizable(0, 0)
    all_rooms_window.configure(bg = rooms_bg)
    cur.execute("SELECT *FROM rooms")
    myresult = cur.fetchall()
    Label(all_rooms_window, text = " ╔══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(all_rooms_window, text = "Rooms", bg = rooms_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(all_rooms_window, text = " ╚══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    #Setting the Table
    tree  =  ttk.Treeview(all_rooms_window, column = ("c1", "c2", "c3","c4","c5",), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Room No")
    tree.column("#2", anchor = CENTER,width = 130)
    tree.heading("#2", text = "Price")
    tree.column("#3", anchor = CENTER,width = 130)
    tree.heading("#3", text = "Status")
    tree.column("#4", anchor = CENTER,width = 100)
    tree.heading("#4", text = "Occupied By")
    tree.column("#5", anchor = CENTER,width = 130)
    tree.heading("#5", text = "Check in Date")
    tree.pack(expand = NO ,pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row)
    Button(all_rooms_window, text = "Close Window", font = "Corbel 10", width = 20, height = 2,bd = 5, command = all_rooms_window.destroy).pack(side = TOP,pady = 15)


def clear_cmd_rooms():
       x="select Room_no from rooms"
       cur.execute(x)
       rlst=cur.fetchall()
       alst=[]
       k=""
       for i in rlst:
           for j in i:
               if j not in "(),":
                   k+=str(j)
           alst.append (j)
          
       rooms_var = StringVar()
       rooms_var.set(alst[0])
       search_by_rooms_window  =  Toplevel()
       search_by_rooms_window.geometry("400x400")
       search_by_rooms_window.resizable(0, 0)
       search_by_rooms_window.title("Search by Room number")
       search_by_rooms_window.configure(bg = rooms_bg)
       Label(search_by_rooms_window, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
       Label(search_by_rooms_window, text = "Search By Room no.",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
       Label(search_by_rooms_window, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
       Label(search_by_rooms_window, text = "", bg = rooms_bg).grid(row = 4)
       Label(search_by_rooms_window, text = "   Enter Room number : ", bg = rooms_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
       def search_rooms():
          searched = rooms_var.get()
          searched = searched.strip()
          if searched != "":
              search_result = Toplevel()
              search_result.title("Search Result")
              search_result.geometry("725x320")
              search_result.resizable(0, 0)
              search_result.configure(bg = rooms_bg)
              Label(search_result, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
              Label(search_result, text = "        Result",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
              Label(search_result, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
              Label(search_result, text = "", bg = rooms_bg).grid(row = 4)
              #Data
              searched = rooms_var.get()
              searched = searched.strip()
              sql = "select * from rooms WHERE Room_no  = '%s';"%searched
              cur.execute(sql)
              myresult  =  cur.fetchall()
              #Showing Result
              result  =  Label(search_result, text = tabulate(myresult, headers = ['Room Number','Price','Status','Membership ID','Check in date'],tablefmt = 'fancy_grid'), bg = rooms_bg, fg = mem_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
              Label(search_result, text = "", bg = rooms_bg).grid(row = 6)
              Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)
          else:
              messagebox.showerror(title="Search Room by Room Number",message="Please choose a room number",parent=search_by_rooms_window)

       rno_entry  =  str(OptionMenu(search_by_rooms_window,rooms_var,*alst).grid(row = 5, sticky = "e"))
       def clear_input():
           rooms_var.set("")
       Label(search_by_rooms_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 6)
       Label(search_by_rooms_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 7)
       Button(search_by_rooms_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_rooms).grid(row = 7, sticky = "w", padx = 30, pady = 20)
       Button(search_by_rooms_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_input).grid(row = 7, sticky = "e", pady = 20)
       Label(search_by_rooms_window, text = " ", bg = rooms_bg).grid(row = 8)
       Button(search_by_rooms_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_rooms_window.destroy).grid(row = 9)
       

def search_cmd_occupancy():
    rlst=["Occupied","Vacant"]
    vac_var = StringVar()
    vac_var.set(rlst[0])
    search_by_vac_window  =  Toplevel()
    search_by_vac_window.geometry("400x400")
    search_by_vac_window.resizable(0, 0)
    search_by_vac_window.title("Search Room by Occupancy")
    search_by_vac_window.configure(bg = rooms_bg)
    Label(search_by_vac_window, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
    Label(search_by_vac_window, text = " Search By Vacancy",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_vac_window, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
    Label(search_by_vac_window, text = "", bg = rooms_bg).grid(row = 4)
    Label(search_by_vac_window, text = "   Enter Occupancy :", bg = rooms_bg,font = "Corbel 14 bold", fg = mem_fg).grid(row = 5, sticky = "w")
    def search_vacancy():
        searched = vac_var.get()
        searched = searched.strip()
        if searched != "":
            search_result = Toplevel()
            search_result.title("Search Result")
            search_result.geometry("600x500")
            search_result.resizable(0, 0)
            search_result.configure(bg = rooms_bg)
            Label(search_result, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
            Label(search_result, text = "        Result",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
            Label(search_result, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
            Label(search_result, text = "", bg = rooms_bg).grid(row = 4)
            #Data
            searched = vac_var.get()
            sql = "select * from rooms WHERE Occupancy  = '%s';"%searched
            cur.execute(sql)
            myresult  =  cur.fetchall()
            #Showing Result
            #Setting the Table
            tree  =  ttk.Treeview(search_result, column = ("c1", "c2", "c3","c4","c5"), show = 'headings')
            tree.column("#1", anchor = CENTER,width = 60)
            tree.heading("#1", text = "Room No,")
            tree.column("#2", anchor = CENTER,width = 130)
            tree.heading("#2", text = "Price")
            tree.column("#3", anchor = CENTER,width = 130)
            tree.heading("#3", text = "Status")
            tree.column("#4", anchor = CENTER,width = 100)
            tree.heading("#4", text = "Occupied By")
            tree.column("#5", anchor = CENTER,width = 130)
            tree.heading("#5", text = "Check in Date")
            tree.grid(padx = 25, pady = 20)
            #Appending the records in the table
            for row in myresult:
                tree.insert("", END, values = row)
            Label(search_result, text = "", bg = rooms_bg).grid(row = 6)
            Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)
        else:
            messagebox.showerror(title = "Search rooms by occupancy", message = "Please select an occupancy status",parent = search_by_vac_window)
    ID_entry  =  (OptionMenu(search_by_vac_window,vac_var,*rlst).grid(row = 5, sticky = "e"))
    def clear_input():
        vac_var.set("")
    Label(search_by_vac_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_vac_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_vac_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_vacancy).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_vac_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_input).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_vac_window, text = " ", bg = rooms_bg).grid(row = 8)
    Button(search_by_vac_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_vac_window.destroy).grid(row = 9)
                   

def makeBill(vac):
    #input("Enter Room Number: ")
    rno = vac
    cur.execute("select * from rooms where room_no = %s" % rno)
    raw_room_details = cur.fetchall()
    temp_cid = raw_room_details[0][4]
    #Room Fee
    temp_fee = raw_room_details[0][1]       #Room number to check out
    #Membership 
    temp_mid = raw_room_details[0][3]#

    #To get Number of days of stay
    sql = "select curdate()"
    cur.execute(sql)
    raw_cur_date = cur.fetchall()
    temp_curdate = raw_cur_date[0][0]
    temp_days = temp_curdate - temp_cid
    #Number of Days
    temp_days = temp_days.days          #Number of Days
    if temp_days == 0:
        temp_days = 1

    #Bill Amount
    temp_amt = temp_days*temp_fee       #Bill Amount

    #Generating Bill Number
    cur.execute("select max(bill_no) from bills")
    raw_last_bill_no = cur.fetchall()
    last_bill_no = raw_last_bill_no[0][0]
    if last_bill_no == None:
        new_bill_no = 10001
    else:
        new_bill_no = last_bill_no +1

    # #BILL SQL EXECUTION
    cur.execute(f"insert into bills values ({new_bill_no}, {rno}, {temp_mid}, {temp_days}, {temp_amt})")
    db.commit()

def check_out_cmd():
       x="select Room_no from rooms where Occupancy='Occupied'"
       cur.execute(x)
       rlst=cur.fetchall()
       alst=[]
       k=""
       for i in rlst:
           for j in i:
               if j not in "(),":
                   k+=str(j)
           alst.append (j)
       vac_var = StringVar()
       vac_var.set(alst[0])
       update_vac_window  =  Toplevel()
       update_vac_window.geometry("400x400")
       update_vac_window.resizable(0, 0)
       update_vac_window.title("Update Room Vacancy")
       update_vac_window.configure(bg = rooms_bg)
       Label(update_vac_window, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
       Label(update_vac_window, text = " Check Out",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
       Label(update_vac_window, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
       Label(update_vac_window, text = "", bg = rooms_bg).grid(row = 4)
       def update_vacancy():
            #SQL Execution
            vac  =  vac_var.get()
            vac = vac.strip()
            if vac != "":
                makeBill(vac)
                cur.execute("update rooms set Occupancy = 'Vacant' where Room_no  = '%s'" %vac)
                myresult  =  cur.fetchall()    
                db.commit()
                cur.execute("update rooms set  membership_id = NULL where Occupancy = 'Vacant'")
                db.commit()
                cur.execute("update rooms set Check_in_date = NULL where Occupancy = 'Vacant'")
                db.commit()
                messagebox.showinfo("Updated Room Status","Room occupancy status was updated and Bill Generated Successfully!!", parent = update_vac_window)
            else:
                messagebox.showerror("Check out","Please select a room number to check out", parent = update_vac_window)
       Label(update_vac_window, text = "Room Number : ", bg = rooms_bg,fg = mem_fg, font = "Corbel 15 bold").grid(row = 5,sticky = 'w',padx = 20)       
       ID_entry  =  str(OptionMenu(update_vac_window,vac_var,*alst).grid(row = 5, sticky = "e",padx = 10))
       def clear_input():
           vac_var.set("")
       clear_input()
       Label(update_vac_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 6)
       Label(update_vac_window, text = " ", bg = rooms_bg, font = "Corbel 20 bold").grid(row = 7)
       Button(update_vac_window, text = "Check Out", font = "Corbel 10", width = 20, height = 2,bd = 5, command = update_vacancy).grid(row = 7, sticky = "w", padx = 30, pady = 20)
       Button(update_vac_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_input).grid(row = 7, sticky = "e", pady = 20)
       Label(update_vac_window, text = " ", bg = rooms_bg).grid(row = 8)
       Button(update_vac_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = update_vac_window.destroy).grid(row = 9)     


def check_in_cmd():
       x="select Room_no from rooms where Occupancy='Vacant'"
       cur.execute(x)
       rlst=cur.fetchall()
       alst=[]
       k=""
       for i in rlst:
           for j in i:
               if j not in "(),":
                   k+=str(j)
           alst.append (j)
       mid_var = StringVar()
       fnm_var = StringVar()
       lnm_var = StringVar()
       bkm_var = StringVar()
       rno_var = StringVar()
       update_vac_window  =  Toplevel()
       update_vac_window.geometry("400x400")
       update_vac_window.resizable(0, 0)
       update_vac_window.title("Check In")
       update_vac_window.configure(bg = rooms_bg)
       Label(update_vac_window, text = "   ╔═══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 1)
       Label(update_vac_window, text = " Check In",bg = rooms_bg, fg = mem_fg, font = "Corbel 20 bold").grid(row = 2)
       Label(update_vac_window, text = "   ╚═══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
       Label(update_vac_window, text = "", bg = rooms_bg).grid(row = 4)
       def update_vacancy():
            #SQL Execution
            mid  =  mid_var.get()
            mid = mid.strip()
            rno = rno_var.get()
            rno = rno.strip()
            if mid and rno != "":
                cur.execute("Select curdate()")
                nowdate = cur.fetchall()
                bkm = nowdate[0][0]
                rno = rno_var.get()
                cur.execute("update rooms set Membership_ID = %s where Room_no = '%s'"%(mid,rno))
                db.commit()
                cur.execute("update rooms set Occupancy = 'Occupied' where Room_no = '%s'"%(rno))
                db.commit()
                cur.execute("update rooms set Check_in_date = '%s' where Room_no = '%s'"%(bkm,rno))
                db.commit()
                messagebox.showinfo("Update Room Status","Room occupancy status was updated! \n '%s' is now occupied by %s" % (rno,mid) , parent = update_vac_window)
            else:
                messagebox.showerror("Check In","Please choose a room number and enter a valid Membership ID", parent = update_vac_window)
       #ROOM NUMBER ENTRY
       Label(update_vac_window, text = "Room Number : ", bg = rooms_bg,font = "Corbel 15 bold", fg = mem_fg).grid(row = 5,sticky = 'w',pady = 10, padx = 10)
       rno_entry  =  (OptionMenu(update_vac_window,rno_var,*alst).grid(row = 5, sticky = "e",pady = 10))
       #MEMBERSHIP ID ENTRY
       Label(update_vac_window, text = "Membership ID : ", bg = rooms_bg,font = "Corbel 15 bold", fg = mem_fg).grid(row = 8,sticky = 'w',pady = 10, padx = 10)
       mid_entry  =  (Entry(update_vac_window, width = 15, font = "Consolas 15",textvariable = mid_var).grid(row = 8, sticky = "e",pady = 10))
       #CLEAR INPUT FUNCTION
       def clear_input():
           rno_var.set("")
           mid_var.set("")
       #BUTTONS
       Label(update_vac_window, text = " ", bg = rooms_bg).grid(row = 11)
       Button(update_vac_window, text = "Check In", font = "Corbel 10", width = 20, height = 2,bd = 5, command = update_vacancy).grid(row = 12, sticky = "w", padx = 25)
       Button(update_vac_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_input).grid(row = 12, sticky = "e")
       Label(update_vac_window, text = " ", bg = rooms_bg).grid(row = 13)
       Button(update_vac_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = update_vac_window.destroy).grid(row = 14)     

           

#SEARCH ROOMS OPTIONS WINDOW      
def display_rooms_options():
      display_rooms_window  =  Toplevel()
      display_rooms_window.geometry("400x400")
      display_rooms_window.resizable(0, 0)
      display_rooms_window.title("Rooms Details Options")
      display_rooms_window.configure(bg = rooms_bg)
      Label(display_rooms_window, text = " ╔══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 20).grid(row = 1)
      Label(display_rooms_window, text = "Search Rooms", bg = rooms_bg,fg = mem_fg, font = "Corbel 20 bold", padx = 90).grid(row = 2)
      Label(display_rooms_window, text = " ╚══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).grid(row = 3)
      Label(display_rooms_window, text = "", bg = rooms_bg).grid(row = 4)
      Button(display_rooms_window, text = "Show All Rooms", width = 20,height = 2, command = display_all_rooms, bd = 5).grid(row = 5)
      Label(display_rooms_window, text = "", bg = rooms_bg).grid(row = 6)
      Button(display_rooms_window, text = "Search By Room Number", width = 20,height = 2, command = clear_cmd_rooms, bd = 5).grid(row = 7)
      Label(display_rooms_window, text = "", bg = rooms_bg).grid(row = 8)
      Button(display_rooms_window, text = "Search By Occupancy", width = 20,height = 2, command = search_cmd_occupancy, bd = 5).grid(row = 9)
      Label(display_rooms_window, text = "", bg = rooms_bg).grid(row = 10)
      Button(display_rooms_window, text = "Close Window", width = 20,height = 2, command = display_rooms_window.destroy, bd = 5).grid(row = 11)
      


#ROOMS MAIN WINDOW
def rooms_window():
    rooms_page  =  Toplevel()
    rooms_page.title("Rooms Window")
    rooms_page.configure(bg = rooms_bg)
    rooms_page.geometry("550x500")
    rooms_page.resizable(0, 0)
    #Getting Data
    cur.execute("SELECT * FROM rooms")
    myresult  =  cur.fetchall()
    def refresh():
        rooms_page.destroy()
        rooms_window()
    #Label
    Label(rooms_page, text = " ╔══════════╗", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg, padx = 25).pack(side = TOP,pady = 10)
    Label(rooms_page, text = "Rooms", bg = rooms_bg, fg = mem_fg,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(rooms_page, text = " ╚══════════╝", bg = rooms_bg,font = "Corbel 20 bold", fg = mem_fg).pack(side = TOP)
    #Refresh Button
    Button(rooms_page, text = " Refresh ⟳", width = 12,height = 1,command = refresh).pack(side = TOP,anchor = "ne",padx = 20)
    #Setting the Table
    tree  =  ttk.Treeview(rooms_page, column = ("c1", "c2", "c3","c4","c5"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Room No.")
    tree.column("#2", anchor = "center",width = 130)
    tree.heading("#2", text = "Price")
    tree.column("#3", anchor = "center",width = 130)
    tree.heading("#3", text = "Status")
    tree.column("#4", anchor = "center",width = 100)
    tree.heading("#4", text = "Occupied By")
    tree.column("#5", anchor = CENTER,width = 100)
    tree.heading("#5", text = "Check in Date")
    tree.pack(expand = YES,pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row)
    # Buttons
    Button(rooms_page, text = "Search Rooms", width = 15, height = 2,command = display_rooms_options, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(rooms_page, text = "Check In", width = 15, height = 2,command = check_in_cmd, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(rooms_page, text = "Check Out", width = 15, height = 2,command = check_out_cmd, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(rooms_page, text = "Close Window", width = 15, height = 2, command = rooms_page.destroy, bd = 5).pack(side = LEFT,padx = 10,pady = 15)

#___________________________________
#Bills WINDOW AND FUNCTIONS

def search_bill_by_bill_no():
    def search_bill_no():
        bno = bno_var.get()
        try:
            bno = int(bno)
            sql = "select * from bills WHERE bill_no  =  %s" % bno
            cur.execute(sql)
            myresult  =  cur.fetchall()
            if myresult !=[]:
                search_result = Toplevel()
                search_result.title("Search Result")
                search_result.geometry("600x320")
                search_result.resizable(0, 0)
                search_result.configure(bg = bills_bg)
                Label(search_result, text = "   ╔═══════════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 1)
                Label(search_result, text = "  Result",bg = bills_bg, fg = bills_fg, font = "Corbel 20 bold").grid(row = 2)
                Label(search_result, text = "   ╚═══════════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 3)
                Label(search_result, text = "", bg = bills_bg).grid(row = 4)
                #Showing Result
                result  =  Label(search_result, text = tabulate(myresult, headers = ['Bill No.', 'Room No', 'Mem. ID', 'Days', 'Amount'], tablefmt = 'fancy_grid'), bg = bills_bg, fg = bills_fg, font = "Consolas 12 ").grid(padx = 20,row = 5)
                Label(search_result, text = "", bg = bills_bg).grid(row = 6)
                Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
            else:
                messagebox.showinfo("Search Bill","No bill found with bill number %s" % bno ,parent = search_by_ID_window)
        except:
            messagebox.showerror("Search Bill","Invalid bill number entered" ,parent = search_by_ID_window)
    def clear_cmd():
        bno_var.set("")
    bno_var = StringVar()
    search_by_ID_window  =  Toplevel()
    search_by_ID_window.geometry("400x400")
    search_by_ID_window.resizable(0, 0)
    search_by_ID_window.title("Search Bill Number")
    search_by_ID_window.configure(bg = bills_bg)
    Label(search_by_ID_window, text = "   ╔═══════════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 1)
    Label(search_by_ID_window, text = "  Search By Bill Number",bg = bills_bg, fg = bills_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_by_ID_window, text = "   ╚═══════════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 3)
    Label(search_by_ID_window, text = "", bg = bills_bg).grid(row = 4)
    Label(search_by_ID_window, text = "    Enter Bill No :", bg = bills_bg,font = "Corbel 14 bold", fg = bills_fg).grid(row = 5, sticky = "w")
    #
    bno_entry  =  (Entry(search_by_ID_window, width = 15, font = "Consolas 14",textvariable = bno_var).grid(row = 5, sticky = "e"))
    #
    Label(search_by_ID_window, text = " ", bg = bills_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_by_ID_window, text = " ", bg = bills_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_by_ID_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_bill_no).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_by_ID_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_by_ID_window, text = " ", bg = bills_bg).grid(row = 8)
    Button(search_by_ID_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_by_ID_window.destroy).grid(row = 9)
    #Label(search_by_ID_window, text = "Membership ID is 5 characters long and is unique to each member",bg = mem_bg, fg = mem_fg, font = "Corbel 8").grid(row = 10, sticky = "sw", pady = 20)


def search_bill_by_mid():
    def search_bill_mid():
        mid = mid_var.get()
        mid = mid.strip()
        try:
            mid = int(mid)
            sql = "select * from bills WHERE mem_id  =  %s" % mid
            cur.execute(sql)
            myresult  =  cur.fetchall()
            if myresult !=[]:
                search_result = Toplevel()
                search_result.title("Search Result")
                search_result.geometry("600x500")
                search_result.resizable(0, 0)
                search_result.configure(bg = bills_bg)
                Label(search_result, text = "   ╔═══════════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 1)
                Label(search_result, text = "  Result",bg = bills_bg, fg = bills_fg, font = "Corbel 20 bold").grid(row = 2)
                Label(search_result, text = "   ╚═══════════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 3)
                Label(search_result, text = "", bg = bills_bg).grid(row = 4)
                #Setting the Table
                tree  =  ttk.Treeview(search_result, column = ("c1", "c2", "c3","c4","c5"), show = 'headings')
                tree.column("c1", anchor = CENTER,width = 60)
                tree.heading("c1", text = "Bill No.")
                tree.column("c2", anchor = "center",width = 130)
                tree.heading("c2", text = "Room No.")
                tree.column("c3", anchor = "center",width = 130)
                tree.heading("c3", text = "Mem. ID")
                tree.column("c4", anchor = "center",width = 100)
                tree.heading("c4", text = "Days")
                tree.column("c5", anchor = CENTER,width = 100)
                tree.heading("c5", text = "Amount")
                tree.grid(padx = 40 ,pady = 20)
                #Appending the records in the table
                for row in myresult:
                    tree.insert("", END, values = row)
                Label(search_result, text = "", bg = bills_bg).grid(row = 6)
                Button(search_result,text = "Close Window",font = "Corbel 10",width = 20,height = 2,bd = 5,command = search_result.destroy).grid(row = 7)                                                                                                                 
            else:
                messagebox.showinfo("Search Bill","No bill found related to member %s" % mid ,parent = search_bill_by_mid_window)
        except:
            messagebox.showerror("Search Bill","Invalid membership ID entered" ,parent = search_bill_by_mid_window)
    def clear_cmd():
        mid_var.set("")
    mid_var = StringVar()
    search_bill_by_mid_window  =  Toplevel()
    search_bill_by_mid_window.geometry("400x400")
    search_bill_by_mid_window.resizable(0, 0)
    search_bill_by_mid_window.title("Search Bills")
    search_bill_by_mid_window.configure(bg = bills_bg)
    Label(search_bill_by_mid_window, text = "   ╔═══════════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 1)
    Label(search_bill_by_mid_window, text = "  Search By Member",bg = bills_bg, fg = bills_fg, font = "Corbel 20 bold").grid(row = 2)
    Label(search_bill_by_mid_window, text = "   ╚═══════════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg).grid(row = 3)
    Label(search_bill_by_mid_window, text = "", bg = bills_bg).grid(row = 4)
    Label(search_bill_by_mid_window, text = "    Enter Membership ID :", bg = bills_bg,font = "Corbel 14 bold", fg = bills_fg).grid(row = 5, sticky = "w")
    #
    mid_entry  =  (Entry(search_bill_by_mid_window, width = 15, font = "Consolas 14",textvariable = mid_var).grid(row = 5, sticky = "e"))
    #
    Label(search_bill_by_mid_window, text = " ", bg = bills_bg, font = "Corbel 20 bold").grid(row = 6)
    Label(search_bill_by_mid_window, text = " ", bg = bills_bg, font = "Corbel 20 bold").grid(row = 7)
    Button(search_bill_by_mid_window, text = "Search", font = "Corbel 10", width = 20, height = 2,bd = 5, command = search_bill_mid).grid(row = 7, sticky = "w", padx = 30, pady = 20)
    Button(search_bill_by_mid_window, text = "Clear", font = "Corbel 10", width = 20,height = 2, bd = 5, command = clear_cmd).grid(row = 7, sticky = "e", pady = 20)
    Label(search_bill_by_mid_window, text = " ", bg = bills_bg).grid(row = 8)
    Button(search_bill_by_mid_window, text = "Close Window", font = "Corbel 10", width = 20,height = 2, bd = 5, command = search_bill_by_mid_window.destroy).grid(row = 9)


#Search Bill
def search_bill():
    search_bills_page  =  Toplevel()
    search_bills_page.geometry("320x380")
    search_bills_page.title("Bills")
    search_bills_page.resizable(0, 0)
    search_bills_page.configure(bg = bills_bg)
    #Label
    Label(search_bills_page, text = " ╔══════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg , padx = 25).grid(row = 1 ,pady = 10)
    Label(search_bills_page, text = "Search Bills", bg = bills_bg, fg = bills_fg ,font = "Corbel 20 bold", padx = 100).grid(row = 2)
    Label(search_bills_page, text = " ╚══════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg ).grid(row = 3)
    Button(search_bills_page, text = "By Bill Number", width = 15, height = 2,command = search_bill_by_bill_no, bd = 5).grid(row = 4,pady = 10)
    Button(search_bills_page, text = "By Member", width = 15, height = 2,command = search_bill_by_mid, bd = 5).grid(row = 5,pady = 10)
    Button(search_bills_page, text = "Close Window", width = 15, height = 2, command = search_bills_page.destroy, bd = 5).grid(row = 6,pady = 10)

    
def bills_window():
    # fg = D6ED17   bg = 606060
    bills_page  =  Toplevel()
    bills_page.geometry("550x500")
    bills_page.title("Bills")
    bills_page.resizable(0, 0)
    bills_page.configure(bg = bills_bg)
    cur.execute("SELECT * FROM bills")
    myresult  =  cur.fetchall()
    #Refresh Button
    def refresh():
        bills_page.destroy()
        bills_window()
    #Label
    Label(bills_page, text = " ╔══════════╗", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg , padx = 25).pack(side = TOP,pady = 10)
    Label(bills_page, text = "Bills", bg = bills_bg, fg = bills_fg ,font = "Corbel 20 bold", padx = 100).pack(side = TOP)
    Label(bills_page, text = " ╚══════════╝", bg = bills_bg,font = "Corbel 20 bold", fg = bills_fg ).pack(side = TOP)
    #Refresh Button
    Button(bills_page, text = " Refresh ⟳", width = 12,height = 1,command = refresh).pack(side = TOP,anchor = "ne",padx = 20)
    #Setting the Table
    tree  =  ttk.Treeview(bills_page, column = ("c1", "c2", "c3","c4","c5"), show = 'headings')
    tree.column("#1", anchor = CENTER,width = 60)
    tree.heading("#1", text = "Bill No.")
    tree.column("#2", anchor = "center",width = 130)
    tree.heading("#2", text = "Room No.")
    tree.column("#3", anchor = "center",width = 130)
    tree.heading("#3", text = "Mem. ID")
    tree.column("#4", anchor = "center",width = 100)
    tree.heading("#4", text = "Days")
    tree.column("#5", anchor = CENTER,width = 100)
    tree.heading("#5", text = "Amount")
    tree.pack(expand = YES,pady = 20)
    #Appending the records in the table
    for row in myresult:
        tree.insert("", END, values = row)
    # Buttons
    Button(bills_page, text = "Search Bill", width = 15, height = 3,command = search_bill, bd = 5).pack(side = LEFT,padx = 10,pady = 15)
    Button(bills_page, text = "Generate Bill", width = 15, height = 3,command = check_out_cmd, bd = 5).pack(side = LEFT,padx = 80,pady = 15)
    Button(bills_page, text = "Close Window", width = 15, height = 3, command = bills_page.destroy, bd = 5).pack(side = RIGHT,padx = 10,pady = 15)

# __________________________________

# Main Window

main_window  =  Tk()
main_window.title("Chamberlain - Main Menu")
main_window.geometry("400x430")
main_window.resizable(0, 0)
main_window.configure(bg = main_bg)
# HEADING
Label(main_window, text = "   Hotel Management System", bg = main_bg,fg = main_fg, font = "HPSimplifiedReg 20 bold", pady = 25).grid(row = 1)
Label(main_window, text = "   »»—————　★　—————«« ", bg = main_bg,fg = main_fg, font = "Corbel 20 bold").grid(row = 2)
# Members list button
Label(main_window, text = "", bg = main_bg).grid(row = 3)
Button(main_window, text = "Members Info", width = 20, height = 2,command = members_window, bd = 5).grid(row = 4, column = 0)
# Rooms Info button
Label(main_window, text = "", bg = main_bg).grid(row = 5)
Button(main_window, text = "Rooms Info", width = 20, height = 2,bd = 5, command = rooms_window).grid(row = 6, column = 0)
#Bills Info button
Label(main_window, text = "", bg = main_bg).grid(row = 7)
Button(main_window, text = "Bills Info", width = 20, height = 2,bd = 5, command = bills_window).grid(row = 8, column = 0)
# Quit Button
Label(main_window, text = "", bg = main_bg).grid(row = 9)
Button(main_window, text = "QUIT", width = 20, height = 2, bd = 5,fg = "red2", command = esc_window).grid(row = 10, column = 0)

############################
############################



# __________________________________
# Database startup

t = str(input("Enter MYSQL password: "))



def qconnect():
    """ Connect to MySQL database """
    try:
        db  =  mysql.connect(host = 'localhost',user = 'root',password = t)
        print('Connected to MySQL database')
        db  =  mysql.connect(host = "localhost", user = "root", passwd = t)
        print("\n ------------------------------ \n  Application Started \n ------------------------------ \n")
    except Error as e:
        main_window.destroy()
        messagebox.showerror("Error","Could not start the application due to error(s)")
        quit()

#___________________________________________________________
  
qconnect()        
db  =  mysql.connect(host = "localhost", user = "root", passwd = t)
cur  =  db.cursor()
cur  =  db.cursor()
cur.execute("show databases")
a = cur.fetchall()
#Check for Database
if ('hotel_management_system',) in a:
    #Change the database
    cur.execute("use hotel_management_system")
    cur.execute("show tables")
    temp_tables_list = cur.fetchall()
    if ('bills',) and ('members',) and ('rooms',) not in temp_tables_list:
        messagebox.showerror("Table Error","One or more table(s) are missing from the database. Please run the setup file")
else:
    #Creates Database and Tables
    cur.execute("create database hotel_management_system")
    db.commit()
    cur.execute("use hotel_management_system")
    cur.execute("create table members(membership_id integer(5) Primary Key, First_name varchar(20) not null, Last_name varchar(20) not null, phone_no char(13) not null unique, Email_ID varchar(35) not null, Points integer default 0);")
    db.commit()
    cur.execute("create table rooms(Room_no char(3) Primary Key,Fee_per_day integer default 1000,Occupancy enum('Occupied','Vacant'),membership_id integer(5) ,Check_in_date date );")
    db.commit()
    cur.execute("CREATE TABLE Bills(Bill_no integer(5) ZEROFILL, Room_no char(3), Mem_ID integer(5),Days integer, Amount integer, PRIMARY KEY (Bill_no), FOREIGN KEY (Room_no) REFERENCES Rooms(Room_no), FOREIGN KEY (Mem_ID) REFERENCES Members(Membership_ID));")
    db.commit()
    messagebox.showinfo("Database Connection","New database was created and is ready to use")
    

#MAIN  
db  =  mysql.connect(host = "localhost", user = "root", passwd = t,database = "hotel_management_system")
cur = db.cursor()

threading.Thread(target = main_window.mainloop())


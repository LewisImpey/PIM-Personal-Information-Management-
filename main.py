from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import tkinter as tk

# === Creating the tk for each window=== #
main_Window = Tk()

tabControl = ttk.Notebook(main_Window)
menubar = Menu(main_Window)
filemenu = Menu(menubar, tearoff=0)

def error_Message(mess):
    messagebox.showerror("Error", mess)

# ========== Manipulating The Database ========== #

def Creating_Database():
    conn = sqlite3.connect('Accounts.db')
    # create a cursor
    c = conn.cursor()
    # Search's for a database with the given parameters
    c.execute(''' 
            SELECT count(name) 
            FROM sqlite_master 
            WHERE type='table' 
            AND name='users' 
            ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] != 1:
        # creates the table
        c.execute("""CREATE TABLE users(
                   UserName text,
                   Password text,
                   FirstName text,
                   LastName text,
                   Email text,
                   PostCode text
           )""")
        current_Users = [
                 ('65214589', 'Password1', 'Jacob', 'Beynon', 'jacobbeynon@yahoo.co.uk', 'CF38 2HL'),
                 ('65213692', 'ILovesThis£', 'James', 'Davids', 'james_davids@outlook.com', 'HJ36 4KL'),
                 ('65215987', 'London09£', 'Lewis', 'Impy', 'lewis-Impy@hotmail.co.uk', 'LM09 2JM'),
                 ('65215523', 'phoneIg98', 'Paul', 'Hill', 'Paul-.Hill@gmail.com', 'CF89 3HM'),
                 ('65213261', 'Orange09$', 'Ryan', 'Smith', 'Ryan.Smith@gmail.co.uk', 'BH67 3ZL')
         ]
        c.executemany("INSERT INTO users VALUES (?,?,?,?,?,?)", current_Users)
    else:
        print("Table has all ready been created")
    conn.commit()
    # Close the connection
    conn.close()

def Searching_Database(item):
    # Connecting to the database
    conn = sqlite3.connect('Accounts.db')
    c = conn.cursor()

def Adding_Database(Usr, Pass, First, Sur, Email, Post):
    # Gets rid off the old table
    if Usr == "" or Pass == "" or First == "" or Sur == "" or Email == "" or Post == "":
        error_Message("All fields must contain information")
    else:
        my_tree.destroy()
        # Connecting to the database
        conn = sqlite3.connect('Accounts.db')
        # create a cursor
        c = conn.cursor()
        c.execute("INSERT INTO users Values (?,?,?,?,?,?)", (Usr, Pass, First, Sur, Email, Post))
        conn.commit()
        conn.close()
        # Re builds the tree containing the new information
        create_Tree()

def Deleting_Database(Item):
    # Connecting to the database
    conn = sqlite3.connect('Accounts.db')
    # create a cursor
    c = conn.cursor()

# ========== Login Page========== #

def Login_Page():
    global log
    usr_Entry = ""
    pass_Entry = ""
    log = Tk()
    log.title("Pim System")
    log.geometry("450x450")
    log.config(bg='light blue')
    log.resizable(True, True)

    user = Label(log, text="Username", font=('arial', 30), bg='light blue')
    user.pack()
    user.place(x=125, y=30)

    entry_Username = Entry(log, font=('arial', 25), width=15, textvariable=usr_Entry)
    entry_Username.pack()
    entry_Username.place(x=90, y=75)

    password = Label(log, text="Password", font=('arial', 30), bg='light blue')
    password.pack()
    password.place(x=125, y=130)

    entry_Password = Entry(log, show="*", font=('arial', 25), width=15, textvariable=pass_Entry)
    entry_Password.pack()
    entry_Password.place(x=90, y=175)

    button_Login = Button(log, text="Login", width=10, font='arial', command=lambda: Logging_In(entry_Username.get(), entry_Password.get()))
    button_Login.pack()
    button_Login.place(x=170, y=230)

def Logging_In(Usr, Pass):
    conn = sqlite3.connect('Accounts.db')
    # create a cursor
    c = conn.cursor()
    c.execute("SELECT UserName FROM users WHERE UserName = ?", (Usr,))
    tmp_Usr = str(c.fetchone())
    if tmp_Usr != "None":
        c.execute("SELECT Password FROM users WHERE Password = ?", (Pass,))
        tmp_Pass = str(c.fetchone())
        if tmp_Pass != "None":
            Menu_Bar(1)
            log.destroy()
        else:
            error_Message("Username or Password is incorrect")
            log.destroy()
    else:
        error_Message("Username or Password is incorrect")
        log.destroy()
    conn.close()

def Logging_Out():
    print("Logging User Out")
    Menu_Bar(0)

# ========== Personal Information System ========== #

def PIM_System_Page():
    global system
    Q_text = ""
    system = Tk()
    system.title("Management system")
    system.geometry("1100x600")
    system.resizable(True, True)

    create_Tree()

    lb_listTitle = Label(system, text="PIM Database", font=('arial', 25))

    tb_Queries = Entry(system, font=('arial', 12), width=15, textvariable=Q_text)

    lb_EntryboxName = Label(system, text="Search for:", font=('arial', 12))
    bt_Search = Button(system, text="Search", width=10, font='arial', command=lambda: Searching_Database(tb_Queries.get()))

    lb_User = Label(system, text="Username", font=('arial', 12))
    tb_User_Entry = Entry(system, font=('arial', 12), width=15)

    lb_First = Label(system, text="Firstname", font=('arial', 12))
    tb_Firstname_Entry = Entry(system, font=('arial', 12), width=15)

    lb_Sur = Label(system, text="Surname", font=('arial', 12))
    tb_Surname_Entry = Entry(system, font=('arial', 12), width=15)

    lb_Email = Label(system, text="Email", font=('arial', 12))
    tb_Email_Entry = Entry(system, font=('arial', 12), width=15)

    lb_Post = Label(system, text="Postcode", font=('arial', 12))
    tb_Postcode_Entry = Entry(system, font=('arial', 12), width=15)

    bt_Add = Button(system, text="Add", width=10, font='arial', command=lambda: Adding_Database(
        tb_User_Entry.get(),
        "000000",
        tb_Firstname_Entry.get(),
        tb_Surname_Entry.get(),
        tb_Email_Entry.get(),
        tb_Postcode_Entry.get())
        )

    # Displays all elements onto window
    lb_listTitle.pack()
    lb_listTitle.place(x=0, y=10)

    lb_EntryboxName.pack()
    lb_EntryboxName.place(x=0, y=50)

    tb_Queries.pack()
    tb_Queries.place(x=100, y=50)

    lb_User.pack()
    lb_User.place(x=0, y=300)
    tb_User_Entry.pack()
    tb_User_Entry.place(x=100, y=300)

    lb_First.pack()
    lb_First.place(x=0, y=350)
    tb_Firstname_Entry.pack()
    tb_Firstname_Entry.place(x=100, y=350)

    lb_Sur.pack()
    lb_Sur.place(x=0, y=400)
    tb_Surname_Entry.pack()
    tb_Surname_Entry.place(x=100, y=400)

    lb_Email.pack()
    lb_Email.place(x=0, y=450)
    tb_Email_Entry.pack()
    tb_Email_Entry.place(x=100, y=450)

    lb_Post.pack()
    lb_Post.place(x=0, y=500)
    tb_Postcode_Entry.pack()
    tb_Postcode_Entry.place(x=100, y=500)

    bt_Add.pack()
    bt_Add.place(x=0, y=570)

    bt_Search.pack()
    bt_Search.place(x=70, y=80)

def create_Tree():
    i = 0
    global my_tree
    my_tree = ttk.Treeview(system)
    my_tree['columns'] = ("Username", "Firstname", "Surname", "Email", "Postcode")
    # Formats the columns
    my_tree.column("#0", width=0)
    my_tree.column("Username", anchor=W, width=120)
    my_tree.column("Firstname", anchor=CENTER, width=120)
    my_tree.column("Surname", anchor=CENTER, width=120)
    my_tree.column("Email", anchor=CENTER, width=200)
    my_tree.column("Postcode", anchor=CENTER, width=120)

    # Adds the title of the columns
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Username", text="Username", anchor=W)
    my_tree.heading("Firstname", text="Firstname", anchor=W)
    my_tree.heading("Surname", text="Surname", anchor=W)
    my_tree.heading("Email", text="Email", anchor=W)
    my_tree.heading("Postcode", text="Postcode", anchor=W)

    # Gathers information from the database, then inputs it into the tree diagram
    conn = sqlite3.connect('Accounts.db')
    # create a cursor
    c = conn.cursor()
    c.execute("SELECT UserName FROM users")
    data_User = c.fetchall()
    c.execute("SELECT Password FROM users")
    data_Pass = c.fetchall()
    c.execute("SELECT FirstName FROM users")
    data_First = c.fetchall()
    c.execute("SELECT LastName FROM users")
    data_Sur = c.fetchall()
    c.execute("SELECT Email FROM users")
    data_Email = c.fetchall()
    c.execute("SELECT PostCode FROM users")
    data_Post = c.fetchall()


    for x in data_User:
        my_tree.insert(parent='', index='end', iid=i, text="", values=(data_User[i], data_First[i], data_Sur[i], data_Email[i],  data_Post[i]))
        i = i + 1

    my_tree.pack()
    my_tree.place(x=300, y=20)

# ========== Front Page ========== #

class front_Page:
    def __init__(self, screen):
        Creating_Database()
        screen.title("PIM Home Page")
        screen.geometry("1200x900")
        title = Label(screen, text="PIM Login", font=('arial', 30))
        title.pack()
        title.place(x=520, y=0)
        Menu_Bar(0)

def Menu_Bar(i):
    menubar = Menu(main_Window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Login", command=Login_Page)
    menubar.add_cascade(label="Account", menu=filemenu)
    main_Window.config(menu=menubar)
    if i == 1:
        filemenu2 = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Logout", command=Logging_Out)
        filemenu.delete("Login")
        filemenu2.add_command(label="Personal Information Management System", command=PIM_System_Page)
        menubar.add_cascade(label="System", menu=filemenu2)


# PIM_System_Page()
run = front_Page(main_Window)

mainloop()

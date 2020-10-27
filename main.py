from tkinter import *
from tkinter import ttk
import tkinter as tk

# This builds the GUI Window
master = tk.Tk()
master.title("Account Login")
master.geometry("200x200")
master.resizable(True, True)
tabControl = ttk.Notebook(master)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

user_textbox = StringVar()
pass_textbox = StringVar()


def password_checking():  # This is used for checking if the details entered by the user are on the database
    un = user_textbox.get()
    pa = pass_textbox.get()
    print("UN:" + un)
    print("PA:" + pa)
    if un == "admin" and pa == "admin":
        createMenu()
        print("Its Working")


def Inventory_Menu():
    title_label = tk.Label(master, text="Welcome").place(x=0, y=0)


def Login_Menu():
    print("Ola")


def createMenu():
    menu_widget = tk.Menu(master)
    menu_widget.add_cascade(label="Login", command=Login_Menu)
    menu_widget.add_command(label="Inventory", command=Inventory_Menu)
    master.config(menu=menu_widget)


# === Login Page elements
user = tk.Label(master, text="UserName").place(x=70, y=20)
password = tk.Label(master, text="Password").place(x=70, y=70)
entry_Username = Entry(master, textvariable=user_textbox).place(x=40, y=50)
entry_Password = Entry(master, show="*", textvariable=pass_textbox).place(x=40, y=100)

button_Login = Button(master, text="Login", width=10, command=password_checking).place(x=60, y=135)



mainloop()


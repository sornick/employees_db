from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from db import *


def SecondHome(parent):
  
    global root
    global ENAME
    global CNP
    global SALARY
    global SEARCH
    global tree
    CNP = StringVar()
    SALARY = StringVar()
    SEARCH = StringVar()
    root = Toplevel(parent)
    #=================================
    root.title("Change data")
    width = 700
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="orange")
    ENAME = StringVar()

    #==================================
    Top = Frame(root, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(root, width=500,  bg="Orange")
    Mid.pack(side=TOP)
    MidLeft = Frame(Mid, width=100)
    MidLeft.pack(side=LEFT, pady=10)
    MidLeftPadding = Frame(Mid, width=370, bg="Orange")
    MidLeftPadding.pack(side=LEFT)
    MidRight = Frame(Mid, width=100)
    MidRight.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    #============================
    lbl_title = Label(Top, text="Change data", font=('arial', 16), width=500)
    lbl_title.pack(fill=X)
    
    lbl_title = Label(MidLeftPadding, text="Please select an item and double click on it", font=('arial', 12,'bold'), width=200)
    lbl_title.pack(fill=X)    
    #=============================
    btn_add = Button(MidLeft, text="ADD NEW",font=('arial', 10 ,'bold'), bg="Orange", command=AddNewWindow) 
    btn_add.pack()
    btn_delete = Button(MidLeft, text=" DELETE  ",font=('arial', 10 ,'bold'),bg="red", command=DeleteData)  
    btn_delete.pack(side=LEFT) 
    #============================
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("enameID", "Name", "CNP", "Salary"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('enameID', text="MemberID", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('CNP', text="CNP", anchor=W)

    tree.heading('Salary', text="Salary", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)
#============================

def Database():   
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `employee` (ename_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ENAME TEXT, CNP TEXT, SALARY TEXT)")
    cursor.execute("SELECT * FROM `employee` ORDER BY `ename` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))    

def SubmitData():
    if  ENAME.get() == "" or CNP.get() == "" or SALARY.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:        
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()  
        cursor.execute("INSERT INTO `employee` (ename, cnp, salary) VALUES(?, ?, ?)",(str(ENAME.get()), str(CNP.get()), str(SALARY.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `employee` ORDER BY `ename` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
       
        ENAME.set("")
        CNP.set("")
        SALARY.set("")     
     
def UpdateData():    
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("employees.db") 
    cursor = conn.cursor()
    
    cursor.execute("UPDATE `employee` SET `ename` = ?, `cnp` = ?, `salary` = ? WHERE `ename_id` = ?", (str(ENAME.get()), str(CNP.get()), str(SALARY.get()),int(ename_id)))
    
    conn.commit()
    cursor.execute("SELECT * FROM `employee` ORDER BY `ename` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    ENAME.set("")
    CNP.set("")
    SALARY.set("")              
    
def OnSelected(event):
    global ename_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    ename_id = selecteditem[0]
    ENAME.set("")
    CNP.set("")
    SALARY.set("")
    
    ENAME.set(selecteditem[1])
    CNP.set(selecteditem[2])
    SALARY.set(selecteditem[3])
    
    UpdateWindow = Toplevel()
    UpdateWindow.title("Change data")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    #====================================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)     
    #===================
    lbl_title = Label(FormTitle, text="Change data", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_ename = Label(ContactForm, text="NAME", font=('arial', 14), bd=5) 
    lbl_ename.grid(row=0, sticky=W)
    lbl_empcnp = Label(ContactForm, text="CNP", font=('arial', 14), bd=5)  
    lbl_empcnp.grid(row=1, sticky=W)
    lbl_salary = Label(ContactForm, text="SALARY", font=('arial', 14), bd=5)  
    lbl_salary.grid(row=2, sticky=W)   
    #===================
    ename = Entry(ContactForm, textvariable=ENAME, font=('arial', 14))
    ename.grid(row=0, column=1)
    empcnp = Entry(ContactForm, textvariable=CNP, font=('arial', 14))
    empcnp.grid(row=1, column=1)
    
    salary = Entry(ContactForm, textvariable=SALARY,  font=('arial', 14))  
    salary.grid(row=3, column=1)     
    #==================
    btn_updatecon = Button(ContactForm, text="Update",font=('arial', 12,'bold'),command=UpdateData)  #
    btn_updatecon.grid(row=6, columnspan=2, pady=10)
#===================================   
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            
            cursor.execute("DELETE FROM `employee` WHERE `ename_id` = %d" % selecteditem[0])
            conn.commit()
               
def AddNewWindow():
    global NewWindow
    ENAME.set("")
    CNP.set("")
    SALARY.set("")
    
    NewWindow = Toplevel()
    NewWindow.title("Change data")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()    
    #===================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)  
    #===================
    lbl_title = Label(FormTitle, text="Adding New Contacts", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_ename = Label(ContactForm, text="Name", font=('arial', 14), bd=5)
    lbl_ename.grid(row=0, sticky=W)
    lbl_cnp = Label(ContactForm, text="CNP", font=('arial', 14), bd=5)
    lbl_cnp.grid(row=1, sticky=W)
    
    lbl_salary = Label(ContactForm, text="Salary", font=('arial', 14), bd=5)
    lbl_salary.grid(row=2, sticky=W)    
    #===================
    ename = Entry(ContactForm, textvariable=ENAME, font=('arial', 14))
    ename.grid(row=0, column=1)
    cnp = Entry(ContactForm, textvariable=CNP, font=('arial', 14))
    cnp.grid(row=1, column=1)    
    
    salary = Entry(ContactForm, textvariable=SALARY,  font=('arial', 14))
    salary.grid(row=3, column=1)   
    #==================
    btn_addcon = Button(ContactForm, text="Save", font=('arial', 12,'bold'), command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)       

if __name__ == '__main__':
    root.mainloop()
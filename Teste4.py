from tkinter import *
import tkinter.messagebox as tkMessageBox

from Teste4b import *
import tkinter.ttk as ttk
from db import *

#====================================
root = Tk() 
root.title("Management of employees")

width = 1100
height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="orange")

# ========================================
USERNAME = StringVar()
PASSWORD = StringVar()
ENAME = StringVar()
CNP = StringVar()
SALARY = StringVar()
SEARCH = StringVar()


def Exit(windowToDestroy):
    result = tkMessageBox.askquestion('Employees database', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes' and windowToDestroy == 'root':
       
        conn.close()
        root.destroy()
        exit()
    elif result == 'yes' and windowToDestroy == 'home':
        Home.destroy()      
        exit()
    
def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Employees database/Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
 # ========================================   
def Home():
    global Home
    Home = Tk() 
    Home.title("Employees database/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Employees database", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)  
    filemenu.add_command(label="Exit", command=lambda: Exit('home')) 
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="orange")    
    
    btn_updateempl1 = Button(Home, text="Add new employee ",font=('arial', 16 ,'bold'), command=ShowAddNew)
    btn_updateempl1.pack(side=TOP, padx=20, pady=20, fill=X)
    
    btn_updateempl2 = Button(Home, text="View all employees ",font=('arial', 16 ,'bold'), command=ShowView)
    btn_updateempl2.pack(side=TOP, padx=20, pady=20, fill=X)
   
    btn_updateempl3 = Button(Home, text="EXIT",font=('arial', 16 ,'bold'), command=lambda: Exit("home"))
    btn_updateempl3.pack(side=TOP, padx=20, pady=20, fill=X)    

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Employees database/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Employee", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_employeename = Label(MidAddNew, text="Name:", font=('arial', 25), bd=10)
    lbl_employeename.grid(row=0, sticky=W)
    lbl_cnp = Label(MidAddNew, text="CNP:", font=('arial', 25), bd=10)
    lbl_cnp.grid(row=1, sticky=W)
    lbl_salary = Label(MidAddNew, text="Salary:", font=('arial', 25), bd=10)
    lbl_salary.grid(row=2, sticky=W)
    employeename = Entry(MidAddNew, textvariable=ENAME, font=('arial', 25), width=15)
    employeename.grid(row=0, column=1)
    employeecnp = Entry(MidAddNew, textvariable=CNP, font=('arial', 25), width=15)
    employeecnp.grid(row=1, column=1)
    employeesalary = Entry(MidAddNew, textvariable=SALARY, font=('arial', 25), width=15)
    employeesalary.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="orange", command=AddNew) # from 2nd module"AddNew 
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNew():    
    cursor.execute("INSERT INTO `employee` (ename, cnp, salary) VALUES(?, ?, ?)", (str(ENAME.get()), str(CNP.get()), str(SALARY.get())))
    conn.commit()
    ENAME.set("")
    CNP.set("")
    SALARY.set("")    
    

def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=900, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=900)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=900)
    MidViewForm.pack(side=RIGHT)
    # =========================
    lbl_text = Label(TopViewForm, text="View Employees", font=('arial', 18), width=800)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=20) #new
    search.pack(side=TOP,  padx=10, fill=X)
    # =========================
    btn_search = Button(LeftViewForm, text="Search",font=('arial', 12 ,'bold'), command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset",font=('arial', 12 ,'bold'), command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete",font=('arial', 12 ,'bold'), command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_update = Button(LeftViewForm, text="Update salary",font=('arial', 12 ,'bold'), command=Update)
    btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_updateempl = Button(LeftViewForm, text="Add employee ",font=('arial', 12 ,'bold'), command=ShowAddNew)
    btn_updateempl.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_updateempl3 = Button(LeftViewForm, text="Change data",font=('arial', 12 ,'bold'), command=lambda: SecondHome(Home)) 
    btn_updateempl3.pack(side=TOP, padx=10, pady=10, fill=X)
    
    btn_exit1 = Button(LeftViewForm, text="EXIT",font=('arial', 12 ,'bold'), command=lambda: Exit('home'))
    btn_exit1.pack(side=TOP, padx=10, pady=10, fill=X)
    # ======================
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("EmployeeID", "Name", "CNP", "Salary"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('EmployeeID', text="EmployeeID",anchor=W)
    tree.heading('Name', text="Name",anchor=W)
    tree.heading('CNP', text="CNP",anchor=W)
    tree.heading('Salary', text="Salary",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    
    DisplayData()

def DisplayData():
    cursor.execute("SELECT * FROM `employee`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `employee` WHERE `ename` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    
def Update():        
    
    DisplayData()    
    cursor.execute("SELECT * FROM `employee`")  
    cursor.execute("UPDATE `employee` SET  `salary` = salary * 0.95")
    fetch = cursor.fetchall()
    conn.commit()     

# update data in database 
def DataUpdate(ename_id="",ename="",cnp="",salary=""):
    DisplayData()    
    cursor.execute("UPDATE `employee` SET ename_id=?,cnp=?,salary=? WHERE ename=?",(ename_id,cnp,salary,ename))  
    conn.commit() 
                   
            
def Delete():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('Employees database', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor.execute("DELETE FROM `employee` WHERE `ename_id` = %d" % selecteditem[0])
            conn.commit()        
   
def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Employees database/View employees")
    width = 800
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def Logout():

    result = tkMessageBox.askquestion('Employees database', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':        
        conn.close()
        root.destroy()
        exit()

def Login(event=None):
    global admin_id
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome() 
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")     
 
def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()
# ==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=lambda: Exit('root'))
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
# ==================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)
# =======================
lbl_display = Label(Title, text="Employees database", font=('arial', 45))
lbl_display.pack()

#========================
if __name__ == '__main__':
    DatabaseInit()
    root.mainloop()
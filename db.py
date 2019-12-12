
from queries import * 
import sqlite3
#============================

global conn, cursor
conn = sqlite3.connect("./employees.db")
cursor = conn.cursor()

def DatabaseInit(): 
        cursor.execute(create_admin_table)
        cursor.execute(create_employee_table)
        cursor.execute(select_admin)
        if cursor.fetchone() is None:
                cursor.execute(add_admin)
                conn.commit()
        
        
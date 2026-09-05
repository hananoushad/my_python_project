import lms
import sqlite3
con = sqlite3.connect("lib.db")
c=con.cursor()
c.execute("PRAGMA foreign_keys = ON")
c.execute('''
CREATE TABLE IF NOT EXISTS Staff (
     sid INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     username TEXT UNIQUE NOT NULL,
     password TEXT NOT NULL,
     role TEXT NOT NULL,
     s_status INTEGER NOT NULL);
''')
c.execute('''
CREATE TABLE IF NOT EXISTS Books (
     bid INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     author TEXT NOT NULL,
     isbn TEXT NOT NULL,
     copies INTEGER NOT NULL,
     b_status INTEGER NOT NULL);
''')
c.execute('''
CREATE TABLE IF NOT EXISTS Member(
     mid INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     email TEXT UNIQUE  NOT NULL,
     phone INTEGER NOT NULL,
     m_status INTEGER NOT NULL);
''')
c.execute('''
    CREATE TABLE IF NOT EXISTS Issue_books(
     tid INTEGER PRIMARY KEY,
     idb INTEGER NOT NULL,
     idm INTEGER NOT NULL,
     issue_date TEXT NOT NULL,
     return_date TEXT NOT NULL,
     status TEXT,
     FOREIGN KEY(idb)REFERENCES Books (bid) ON DELETE CASCADE,
     FOREIGN KEY(idm)REFERENCES Member (mid) ON DELETE CASCADE
     );
''')

# c.execute("""INSERT INTO Staff(name,username,password,role,s_status)
#           VALUES("Arun","arun@123","arun123","admin",1);""")
while True:
    print("1:Login")
    print("2:Exit")
    c1=input("Enter your choice:")
    if c1 == "1":
        lms.login()
    elif c1 == "2":
        break
    else:
        print("Invalid choice")
#

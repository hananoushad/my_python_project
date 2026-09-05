# from datetime import datetime
import sqlite3
import datetime
con = sqlite3.connect("lib.db")
c=con.cursor()
def login():
    ul = input("Enter your username: ")
    pl = input("Enter your password: ")
    c.execute("SELECT * FROM Staff WHERE username = ? AND password=?", (ul, pl))
    vl = c.fetchone()
    if vl:
        print("Hello", vl[1])
        if vl[4] == "admin":
            while True:
                print("1:Add staff")
                print("2:Remove staff")
                print("3:View staff details")
                print("4:View books")
                print("5:Log out")
                choiceA = int(input("Enter your choice: "))
                if choiceA == 1:
                    reg()
                elif choiceA == 2:
                    edit_rmv_staff()
                elif choiceA == 3:
                    view_staff()
                elif choiceA == 4:
                    view_books()
                elif choiceA == 5:
                    break
                else:
                    print("Invalid choice")
        if vl[4]=="staff":
            while True:
                print("1:Add members")
                print("2:Remove members")
                print("3:View members")
                print("4:Add books")
                print("5:Remove books")
                print("6:View books")
                print("7:issue books")
                print("8:Renew date")
                print("9:Return books")
                print("10:Log out")
                choiceS=int(input("Enter your choice: "))
                if choiceS == 1:
                    add_members()
                elif choiceS == 2:
                    remove_members()
                elif choiceS == 3:
                    view_members()
                elif choiceS == 4:
                    add_books()
                elif choiceS == 5:
                    remove_books()
                elif choiceS == 6:
                    view_books()
                elif choiceS == 7:
                    issue_books()
                elif choiceS==8:
                    renew_date()
                elif choiceS==9:
                    return_book()
                elif choiceS == 10:
                    break
                else:
                    print("Invalid choice")


    else:

        print("Invalid username or password")
def reg():
    name=input("Enter name: ")
    ur=input("Enter username: ")
    pr=input("Enter password: ")
    role=input("Enter role: ")
    c.execute('''INSERT INTO Staff(name,username,password,role,s_status)
    VALUES(?,?,?,?,1);
    ''', (name, ur,pr, role))
    con.commit()
    print("------user created------")
def edit_rmv_staff():
    staff_id = int(input("Enter the staff ID: "))
    if staff_id:
        c.execute('UPDATE Staff SET s_status=0 WHERE sid=?', (staff_id,))
        con.commit()
        print("------Staff removed!------")
    else:
        print("wrong id")


def view_staff():
    c.execute('SELECT * FROM Staff WHERE s_status=1')
    print("--------------------------------")
    for i in c.fetchall():
            print(i[0], i[1], i[2], i[3])
    print("--------------------------------")
def add_members():
    mem_name=input("Enter member name: ")
    mem_email=input("Enter member email: ")
    mem_phone=input("Enter member phone number: ")
    c.execute('''INSERT INTO Member (name,email,phone,m_status)
        VALUES(?,?,?,1);
        ''', (mem_name, mem_email,mem_phone))
    con.commit()
    print("------Member created!------")
def remove_members():
    member_id = int(input("Enter the Member ID: "))
    if member_id:
        c.execute('UPDATE Member SET m_status=0 WHERE mid=?', (member_id,))
        con.commit()
        print("------member removed!------")
    else:
        print("wrong id")
def view_members():
    c.execute('SELECT * FROM Member')
    print("--------------------------------")
    for i in c.fetchall():
        if i[4] == 1:
            print(i[0], i[1], i[2], i[3])
    print("--------------------------------")
def add_books():
    book_name=input("Enter book name: ")
    author=input("Enter book author: ")
    isbn=input("Enter book ISBN: ")
    n=int(input("Enter number of copies available: "))
    c.execute('''INSERT INTO Books (name,author,isbn,copies,b_status)
    VALUES(?,?,?,?,1);
    ''',(book_name,author,isbn,n))
    con.commit()
    print("------Book added!-------")
def remove_books():
    book_id = int(input("Enter the book ID: "))
    if book_id:
        c.execute('UPDATE Books SET b_status=0 WHERE bid=?',(book_id,))
        con.commit()
        print("------Book removed!------")
    else:
        print("wrong id")
def view_books():
    c.execute("SELECT * FROM Books")
    print("--------------------------------")
    for i in c.fetchall():
        if i[5] == 1:
            print(i[0], i[1], i[2], i[3],i[4])
    print("--------------------------------")
def issue_books():
    id_m=int(input("enter the id of the member:"))
    id_b=int(input("enter the id of the book:"))

    c.execute("SELECT copies FROM Books WHERE bid=?",(id_b,))
    no_copies=c.fetchone()[0]

    if no_copies:
        t = datetime.date.today()
        e = t + datetime.timedelta(days=10)
        c.execute('''INSERT INTO Issue_books (idb,idm,issue_date,return_date)
               VALUES(?,?,?,?);
               ''',(id_b,id_m,t,e))
        con.commit();
        no_copies-=1
        c.execute("UPDATE Books SET copies=? Where bid=?",(no_copies,id_b))
        con.commit()
        print("------Book issued!------")
    else:
        print("Not available")
def renew_date():
    id_mem=int(input("enter the id of the member:"))
    id_book=int(input("enter the id of the book:"))
    c.execute("SELECT return_date FROM Issue_books WHERE idm=? and idb=?",(id_mem,id_book))
    d=c.fetchone()[0]
    # print(d)
    dt_object = datetime.datetime.strptime(d, "%Y-%m-%d")
    # print(dt_object)
    date_obj = dt_object.date()
    # print(date_obj)
    renew_date=date_obj+datetime.timedelta(days=10)
    c.execute("UPDATE Issue_books SET return_date=? Where idm=? and idb=?",(renew_date,id_mem,id_book))
    con.commit()
    print("------Date renewed!-------")
def return_book():
    id_member=int(input("enter the member ID:"))
    id_book=int(input("enter the book ID:"))
    c.execute("UPDATE Issue_books SET status='returned' Where idm=? and idb=?", ( id_member,id_book))
    con.commit()
    c.execute("SELECT copies FROM Books WHERE bid=?", (id_book,))
    no_copies = c.fetchone()[0]
    no_copies=no_copies + 1
    c.execute("UPDATE Books SET copies=? Where bid=?", (no_copies, id_book))
    con.commit()
    print("------Book returned!------")






    
              

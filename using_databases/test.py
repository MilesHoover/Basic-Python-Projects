import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fName TEXT, \
        col_lName TEXT, \
        col_Email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Persons(col_fName, col_lName, col_Email) VALUES (?,?,?)", \
                ("Bob", "Smith", "bsmith@gmail.com"))
    cur.execute("INSERT INTO tbl_Persons(col_fName, col_lName, col_Email) VALUES (?,?,?)", \
                ("Sarah", "Jones", "sjones@gmail.com"))
    cur.execute("INSERT INTO tbl_Persons(col_fName, col_lName, col_Email) VALUES (?,?,?)", \
                ("Sally", "May", "smay@gmail.com"))
    cur.execute("INSERT INTO tbl_Persons(col_fName, col_lName, col_Email) VALUES (?,?,?)", \
                ("Kevin", "Bacon", "kbacon@gmail.com"))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fName, col_lName, col_Email FROM tbl_Persons WHERE col_fName = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name : {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
    

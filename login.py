import sqlite3

conn = sqlite3.connect('login.db')
c = conn.cursor()
valid  = False
taken = False
loggedIn = False
userName = False

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')

def data_entry(username, password):
    c.execute("INSERT INTO login (username, password) VALUES (?, ?)",
              (username, password))
    conn.commit()
    c.close()
    conn.close()

def register():
    global valid, taken
    while not valid:
        c.execute("SELECT * FROM login")
        taken = False
        username = input("username: ")   
        for row in c.fetchall():
            if str(username) == str(row[0]):
                print("that username is already being used")
                taken = True
        if not taken:
            valid = True
    password = input("password: ")
    data_entry(username, password)

def login():
    global loggedIn, userName
    while not loggedIn:
        username = input("username: ")   
        c.execute("SELECT * FROM login")
        for row in c.fetchall():
            if str(username) == str(row[0]):
                password = input("password: ")
                userName = True
                if str(password) == str(row[1]):
                    loggedIn = True
                    break
                else:
                    print("incorrect password")
        if not userName:
            print("incorrect username")
    print("you have logged in!")
        
def startup():
    create_table()
    choice  = input("do you want to login(1) or register(2) type 1 or 2 to answer")
    if choice == '1':
        login()
    else:    
        register()

startup()


import sqlite3 # Import sqlite3 library

# Create database function
def create_db():
    con = sqlite3.connect(database = r'ims.db') # Creates connection to the given database
    cur = con.cursor() # Allows data from database to be fetched and execute SQL queries
    cur.execute('CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, category text, dtype text, location text, age text, vtpye text)') # Create a database with following elements
    con.commit() # Save changes made

    cur.execute('CREATE TABLE IF NOT EXISTS supplier(id INTEGER PRIMARY KEY AUTOINCREMENT, category text, dtype text, solution text)') # Create a database with the following elements
    con.commit()

    cur.execute('CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY AUTOINCREMENT, category text, dtype text, item text, price text)') # Create a database with the following elements
    con.commit()

    cur.execute('CREATE TABLE IF NOT EXISTS report(id INTEGER PRIMARY KEY AUTOINCREMENT, category text, dtype text, success text)') # Create a database with the following elements
    con.commit()


create_db() # Creates database

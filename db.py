import sqlite3
from flask import g
import os

# Create the data folder if it does not exist
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
DATABASE = 'data/example.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        create_db()
    return db

def create_db():
    """Create the database tables."""
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            filepath TEXT
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fileid INTEGER,
            userid TEXT,
            platform TEXT,
            no_of_tests INTEGER,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, completed INTEGER DEFAULT 0,
            FOREIGN KEY (fileid) REFERENCES files (id)
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Options (name TEXT UNIQUE NOT NULL)
        """)
        #Get an entry from the 'options' table in the database where the entry has name 'FPGA'
        someName = 'FPGA'
        cur.execute('SELECT name FROM options WHERE name=?', (someName,))
        result = cur.fetchone()
        
        #If no entry in 'options' table that has name 'FPGA', then insert the option names
        if result is None:
            #Note the comma after 'FPGA'. This creates a tuple with a single element. If you omit the comma, Python
            #  will interpret the parentheses as a grouping operator, and the result will not be a tuple.
            cur.execute("INSERT INTO options (name) VALUES (?)", ('FPGA',))
            cur.execute("INSERT INTO options (name) VALUES (?)", ('Chip Whisperer',))

        cur.execute("""
            CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_path TEXT,
            job_id INTEGER,
            FOREIGN KEY (job_id) REFERENCES jobs (id)
            )
        """)

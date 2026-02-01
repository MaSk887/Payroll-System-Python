#database_config.py
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'payroll.db')
mydp = sqlite3.connect(db_path)
cursor = mydp.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        EmployeeID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,
        Status TEXT,
        Salary REAL
        )
'''
)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS financial_obligations (
        Ob_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EmployeeID INTEGER,
        Category TEXT,
        Amount REAL,
        DueDate TEXT
    )
''')
mydp.commit()
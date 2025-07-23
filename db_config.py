

import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=LAPTOP-8MA1M6E0\\SQLEXPRESS;'
        'DATABASE=InternDB;'
        'Trusted_Connection=yes;'
    )
    return conn

def select_employees():
    conn = get_connection()
    cursor = conn.cursor()
    
    # SELECT query
    cursor.execute("SELECT * FROM Employees")
    
    # Fetch all results
    rows = cursor.fetchall()
    
    # Print each row
    for row in rows:
        print(row)
    
    # Cleanup
    cursor.close()
    conn.close()

# Call the function
select_employees()

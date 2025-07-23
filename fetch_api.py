import requests
import pyodbc

# Step 1: Fetch from Agify API
name = "michael"
response = requests.get(f"https://api.agify.io?name={name}")
data = response.json()

# Extract fields
name = data['name']
age = data['age']
count = data['count']

# Step 2: Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=LAPTOP-8MA1M6E0\\SQLEXPRESS;'
    'DATABASE=InternDB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Step 3: Create table if not exists
cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_NAME = 'AgifyData'
)
BEGIN
    CREATE TABLE AgifyData (
        id INT IDENTITY(1,1) PRIMARY KEY,
        name NVARCHAR(100),
        predicted_age INT,
        sample_count INT
    )
END
""")
conn.commit()

# Step 4: Insert data into table
cursor.execute("INSERT INTO AgifyData (name, predicted_age, sample_count) VALUES (?, ?, ?)",
               name, age, count)
conn.commit()

print(f"Inserted: Name = {name}, Age = {age}, Count = {count}")

# Step 5: Clean up
cursor.close()
conn.close()

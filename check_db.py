
import sqlite3
import os

db_path = os.path.join("backend", "zoff_scope_v3.db")
print(f"Checking database at: {db_path}")

if not os.path.exists(db_path):
    print("Database file not found!")
    exit(1)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)
    
    # Check stores
    try:
        cursor.execute("SELECT count(*) FROM stores")
        count = cursor.fetchone()[0]
        print(f"Number of stores: {count}")
        
        if count > 0:
            cursor.execute("SELECT * FROM stores LIMIT 5")
            rows = cursor.fetchall()
            print("First 5 stores:", rows)
    except sqlite3.OperationalError as e:
        print(f"Error querying stores: {e}")

    conn.close()
except Exception as e:
    print(f"Error: {e}")

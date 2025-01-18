# 





# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('appointments.db')

# # Create table
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS appointments (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL,
#         phone TEXT NOT NULL,
#         doctor TEXT NOT NULL,
#         date TEXT NOT NULL,
#         time TEXT NOT NULL,
#         message TEXT
#     )
# ''')

# conn.commit()
# conn.close()
# print("Database initialized and table created!")



import sqlite3

conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()

# Fetch and display all records
cursor.execute('SELECT * FROM appointments')
appointments = cursor.fetchall()

print("\n--- Appointments in Database ---")
for appointment in appointments:
    print(appointment)

conn.close()

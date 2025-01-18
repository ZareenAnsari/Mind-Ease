# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('appointments.db')
# cursor = conn.cursor()

# # Fetch all records
# cursor.execute("SELECT * FROM appointments")
# appointments = cursor.fetchall()

# # Print the records
# for appointment in appointments:
#     print(appointment)

# conn.close()



import sqlite3

# Connect to the database
conn = sqlite3.connect('appointments.db')
cursor = conn.cursor()

# Fetch all data
cursor.execute('SELECT * FROM appointments')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

# from flask import Flask, request, jsonify # type: ignore
# import sqlite3

# app = Flask(__name__)

# # Ensure the database and table exist
# def initialize_database():
#     conn = sqlite3.connect('appointments.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS appointments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT NOT NULL,
#             doctor TEXT NOT NULL,
#             date TEXT NOT NULL,
#             time TEXT NOT NULL,
#             message TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Route to submit an appointment
# @app.route('/submit-appointment', methods=['POST'])
# def submit_appointment():
#     try:
#         # Get data from the form
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         doctor = request.form.get('doctor')
#         date = request.form.get('date')
#         time = request.form.get('time')
#         message = request.form.get('message', '')

#         # Validate required fields
#         if not (name and email and phone and doctor and date and time):
#             return jsonify({"error": "All fields except message are required"}), 400

#         # Insert data into the database
#         conn = sqlite3.connect('appointments.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO appointments (name, email, phone, doctor, date, time, message)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (name, email, phone, doctor, date, time, message))
#         conn.commit()
#         conn.close()

#         return jsonify({"message": "Appointment booked successfully!"}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Route to fetch all appointments for debugging
# @app.route('/appointments', methods=['GET'])
# def get_appointments():
#     conn = sqlite3.connect('appointments.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM appointments')
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify(rows)

# if __name__ == '__main__':
#     initialize_database()
#     app.run(debug=True)




# from flask import Flask, request, jsonify
# import sqlite3

# app = Flask(__name__)

# # Initialize the database
# def initialize_database():
#     conn = sqlite3.connect('appointments.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS appointments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL,
#             phone TEXT NOT NULL,
#             doctor TEXT NOT NULL,
#             date TEXT NOT NULL,
#             time TEXT NOT NULL,
#             message TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Endpoint to submit an appointment
# @app.route('/submit-appointment', methods=['POST'])
# def submit_appointment():
#     try:
#         # Get data from the form
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         doctor = request.form['doctor']
#         date = request.form['date']
#         time = request.form['time']
#         message = request.form.get('message', '')

#         # Insert the data into the database
#         conn = sqlite3.connect('appointments.db')
#         cursor = conn.cursor()
#         cursor.execute('''
#             INSERT INTO appointments (name, email, phone, doctor, date, time, message)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (name, email, phone, doctor, date, time, message))
#         conn.commit()
#         conn.close()

#         return jsonify({"message": "Appointment booked successfully!"}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Endpoint to view all appointments
# @app.route('/appointments', methods=['GET'])
# def get_appointments():
#     conn = sqlite3.connect('appointments.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM appointments')
#     rows = cursor.fetchall()
#     conn.close()
#     return jsonify(rows)

# if __name__ == '__main__':
#     initialize_database()
#     app.run(debug=True)





from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Route for rendering the form (optional if the form is static)
@app.route('/appointment', methods=['GET'])
def appointment_form():
    return render_template('Appointment.html')

# Route for handling form submission
@app.route('/submit-appointment', methods=['POST'])
def submit_appointment():
    # Fetch form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    doctor = request.form['doctor']
    date = request.form['date']
    time = request.form['time']
    message = request.form.get('message', '')

    # Save data into the database
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (name, email, phone, doctor, date, time, message)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, doctor, date, time, message))
    conn.commit()
    conn.close()

    return "Appointment booked successfully! <a href='/appointment'>Book Another</a>"

if __name__ == '__main__':
    app.run(debug=True)

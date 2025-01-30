from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to the SQLite database
DATABASE = 'submissions.db'

# Function to initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
                query TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database when the app starts
init_db()

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get JSON data from the request
    data = request.get_json()

    # Log the received data to the console (for debugging)
    print("Received data:", data)

    # Save the data to the SQLite database
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO submissions (name, age, phone, query, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['name'], data['age'], data['phone'], data['query'], data['email']))
        conn.commit()

    # Send a success response back to the front-end
    return jsonify({
        "message": "Form submitted successfully!",
        "received_data": data  # Optional: Send the received data back
    })

# Route to view all submissions (optional, for debugging)
@app.route('/submissions', methods=['GET'])
def view_submissions():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM submissions')
        submissions = cursor.fetchall()

    return jsonify({
        "submissions": submissions
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
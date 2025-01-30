from flask import Flask, request, jsonify
from flask_cors import CORS
import json  # Import the json module to work with JSON files
import os  # Import the os module to handle file paths

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to the JSON file where data will be saved
DATA_FILE = 'submissions.json'

# Ensure the JSON file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)  # Initialize with an empty list

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get JSON data from the request
    data = request.get_json()

    # Log the received data to the console (for debugging)
    print("Received data:", data)

    # Load existing data from the JSON file
    with open(DATA_FILE, 'r') as file:
        submissions = json.load(file)

    # Add the new submission to the list
    submissions.append(data)

    # Save the updated list back to the JSON file
    with open(DATA_FILE, 'w') as file:
        json.dump(submissions, file, indent=4)  # Use indent for pretty formatting

    # Send a success response back to the front-end
    return jsonify({
        "message": "Form submitted successfully!",
        "received_data": data  # Optional: Send the received data back
    })

# Route to view all submissions (optional, for debugging)
@app.route('/submissions', methods=['GET'])
def view_submissions():
    # Load data from the JSON file
    with open(DATA_FILE, 'r') as file:
        submissions = json.load(file)

    return jsonify({
        "submissions": submissions
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
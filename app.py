# flask_app.py

from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for students
students = [
    {"name": "John Doe", "prn": "PRN123456"},
    {"name": "Jane Smith", "prn": "PRN654321"},
    {"name": "Alice Johnson", "prn": "PRN987654"},
    {"name": "Bob Lee", "prn": "PRN456789"},
    {"name": "Bidakshita","prn":"PRN457690"},
    {"name": "karan","prn":"PRN5678912"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({"students": students})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

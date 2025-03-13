import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

print("✅ Employee Service 1 Starting...")

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Mayangyan14.",  
    database="freshmart_db"  
)

@app.route('/employees', methods=['GET'])
def get_employees():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, position FROM employees")
    employees = cursor.fetchall()
    
    return jsonify([{"id": emp[0], "name": emp[1], "position": emp[2]} for emp in employees])

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    cursor = db.cursor()
    cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", (data["name"], data["position"]))
    db.commit()
    
    return jsonify({"message": "Employee added successfully"}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # Employee Service 1 on port 5000

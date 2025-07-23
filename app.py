
from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)

# Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees")
    rows = cursor.fetchall()
    employees = [{'id': row[0], 'name': row[1], 'email': row[2], 'age': row[3]} for row in rows]
    conn.close()
    return jsonify(employees)

# Add new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Employees (name, email, age) VALUES (?, ?, ?)", 
                   data['name'], data['email'], data['age'])
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee added successfully"}), 201

# Update employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Employees SET name = ?, email = ?, age = ? WHERE id = ?
    """, data['name'], data['email'], data['age'], id)
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee updated successfully"})

# Delete employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employees WHERE id = ?", id)
    conn.commit()
    conn.close()
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

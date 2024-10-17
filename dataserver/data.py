from flask import Flask, request, jsonify
import mysql.connector  # Import MySQL connector to interact with MySQL database

# Initialize Flask app
app = Flask(__name__)

# Function to connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="mysql",   # This is the service name for the MySQL container in Docker
        user="root",       # MySQL root user
        password="Kartik@2025v",  # MySQL root password (set in Docker Compose)
        database="microservices_db"  # The name of the database
    )

# Define a POST endpoint to add data
@app.route('/data', methods=['POST'])
def add_data():
    data = request.json['data']  # Extract data from the incoming JSON request
    db = connect_db()  # Connect to MySQL
    cursor = db.cursor()  # Create a cursor to execute SQL commands
    # Insert the data into the `items` table
    cursor.execute("INSERT INTO items (data) VALUES (%s)", (data,))
    db.commit()  # Commit the transaction to save the changes
    cursor.close()  # Close the cursor
    db.close()  # Close the database connection
    # Return a success message with status code 201 (Created)
    return jsonify({"message": "Data added successfully"}), 201

# Define a GET endpoint to retrieve all data
@app.route('/', methods=['GET'])
def get_all_data():
    db = connect_db()  # Connect to MySQL
    cursor = db.cursor()  # Create a cursor
    # Retrieve all rows from the `items` table
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()  # Fetch all results from the query
    cursor.close()  # Close the cursor
    db.close()  # Close the database connection
    # Return the result as a JSON response
    return jsonify(result), 200

# Start the Flask app
if __name__ == '__main__':
    # Set the host to '0.0.0.0' to make the app accessible outside the container
    app.run(host='0.0.0.0', port=5000)

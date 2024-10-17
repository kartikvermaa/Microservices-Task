from flask import Flask, jsonify
import requests  # Import requests to make HTTP requests to other services

# Initialize Flask app
app = Flask(__name__)

# Define a GET endpoint to fetch data from the dataserver
@app.route('/', methods=['GET'])
def get_data():
    # Make a GET request to the dataserver's / endpoint to retrieve data
    response = requests.get('http://dataserver:5000/')
    # Return the response from dataserver to the client
    return jsonify(response.json()), response.status_code

# Start the Flask app
if __name__ == '__main__':
    # Set the host to '0.0.0.0' to make the app accessible outside the container
    app.run(host='0.0.0.0', port=5002)

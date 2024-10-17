from flask import Flask, request, jsonify
import requests  # Import requests to make HTTP requests to other services

# Initialize Flask app
app = Flask(__name__)

# Define a POST endpoint to send data to the dataserver
@app.route('/', methods=['POST'])
def post_data():
    data = request.json['data']  # Extract data from the incoming JSON request
    # Make a POST request to the dataserver's /data endpoint to send the data
    response = requests.post('http://dataserver:5000/data', json={"data": data})
    # Return the response from dataserver to the client
    return jsonify({"message": response.json()['message']}), response.status_code

# Start the Flask app
if __name__ == '__main__':
    # Set the host to '0.0.0.0' to make the app accessible outside the container
    app.run(host='0.0.0.0', port=5001)

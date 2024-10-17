# Use the official Python 3.9 image from Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies listed in requirements.txt
RUN pip install -r requirements.txt

RUN pip install werkzeug==2.0.3


# Copy all files from the current directory on the host to the container
COPY . .

# Define the command to run the app (this starts the Flask server)
CMD ["python", "get.py"]

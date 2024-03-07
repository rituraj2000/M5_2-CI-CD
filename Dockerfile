# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code
COPY . .

# Set the environment variables for PostgreSQL connection
ENV DB_HOST=0.0.0.0 \
    DB_NAME=rituraj_db \
    DB_USER=rituraj_db_user \
    DB_PASSWORD=rituraj_db_pass

# Expose the port for the Flask app
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
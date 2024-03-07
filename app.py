import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
DB_HOST = os.environ.get("DB_HOST", "db")
DB_NAME = os.environ.get("DB_NAME", "your_db_name")
DB_USER = os.environ.get("DB_USER", "your_db_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "your_db_password")

@app.route("/")
def index():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        
        # Close the connection
        conn.close()
        
        # Return a JSON response indicating a successful connection
        return jsonify({"status": "OK 👌"})
    except (Exception, psycopg2.Error) as error:
        # Return an error message if the connection fails
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
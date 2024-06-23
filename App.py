from flask import Flask, jsonify
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection details from environment variables
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
driver = '{ODBC Driver 17 for SQL Server}'

try:
    # Establish database connection
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

except pyodbc.Error as e:
    print(f"ODBC Error: {e}")
    conn = None

except Exception as e:
    print(f"Error: {e}")
    conn = None

@app.route('/')
def home():
    if conn:
        return "API is working"
    else:
        return "Database connection failed"

if __name__ == '__main__':
    app.run(debug=True, port=5000)

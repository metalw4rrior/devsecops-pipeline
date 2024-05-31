from flask import Flask, request, render_template_string
import sqlite3
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Hardcoded secret for testing purposes
SECRET_KEY = "supersecretkey"

# Database setup
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES ("admin"), ("guest"), ("user1")')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def hello():
    return "Hello, DevSecOps!"

@app.route('/greet/<name>')
def greet(name):
    # XSS vulnerability
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

@app.route('/users')
def users():
    # SQL Injection vulnerability
    name = request.args.get('name', '')
    query = f"SELECT * FROM users WHERE name = '{name}'"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return {'users': result}

@app.route('/add_user', methods=['POST'])
def add_user():
    # Unvalidated input and hardcoded secret
    name = request.form['name']
    if name == SECRET_KEY:
        return "Invalid username!", 400
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return "User added!", 201

@app.route('/file')
def get_file():
    # Path traversal vulnerability
    filename = request.args.get('filename')
    with open(f"./files/{filename}", "r") as f:
        content = f.read()
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)








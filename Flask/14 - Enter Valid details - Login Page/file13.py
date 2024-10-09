# This is like login page with Database

from flask import Flask, request, render_template, redirect, url_for
import pyodbc
from flask import flash

app = Flask(__name__)
app.secret_key = "hari_tutorial"    

# Database connection details
def get_db_connection():
    connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=DESKTOP-6KV2EF8;"
                          "Database=log_in;"
                          "Trusted_Connection=yes;")
    return connection

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

    
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (user, pwd))
        account = cursor.fetchone()

        if account:
            return redirect(url_for('dashboard'))
        else:
            flash("Wrong Details !!" , 'error')
            return render_template('error.html')
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

if __name__ == '__main__':
    app.run(debug=True)

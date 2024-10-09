from flask import Flask, request, render_template , redirect , url_for , jsonify
import pyodbc

app = Flask(__name__)


# Database connection
def get_db_connection():
    connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=DESKTOP-6KV2EF8;"
                          "Database=form;"
                          "Trusted_Connection=yes;")
    return connection

@app.route('/')
def index():
    return render_template('admin.html')


@app.route('/register')
def register():
    return render_template("form.html")


@app.route('/details', methods=['POST'])
def add_record():
    if request.method == 'POST':
        User_name = request.form['text']
        Email = request.form['email']
        Password = request.form['password']
        Confirm_password = request.form['confirm_password']


        if not User_name or not Email or not Password or not Confirm_password:
            return jsonify({"error": "All fields are required"})
        if Password != Confirm_password:
            return jsonify({"error": "Password must me same"})
        

        #  Connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # Cursor.execute
        cursor.execute("INSERT INTO login_details (user_name , Email , Password , Confirm_password) VALUES (?, ? , ? , ? )", (User_name, Email , Password , Confirm_password))
        connection.commit()

        # Close the cursor  &  connection
        cursor.close()
        connection.close()
    
    return 'Record added successfully!'



#  Log_in details

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Email = request.form['email']
        pwd = request.form['password']

    
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM login_details WHERE Email = ? AND Password = ?', (Email, pwd))
        account = cursor.fetchone()

        if account:
            return redirect(url_for('dashboard'))
        else:
            return "Wrong details !!! "
        
    return render_template('login.html')



@app.route('/database')
def dashboard():
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)

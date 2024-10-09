# How to Store the give details in HTML to SQL Database ( Register Form )

from flask import Flask, request, render_template
import pyodbc

app = Flask(__name__)

# Database connection
def get_db_connection():
    connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=DESKTOP-6KV2EF8;"
                          "Database=freefire;"
                          "Trusted_Connection=yes;")
    return connection

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_record():
    player_id = request.form['player_id']
    player_name = request.form['player_name']
    
    #  Connection
    connection = get_db_connection()
    cursor = connection.cursor()

    # Cursor.execute
    cursor.execute("INSERT INTO player_details (player_id, player_name) VALUES (?, ?)", (player_id, player_name))
    connection.commit()

    # Close the cursor  &  connection
    cursor.close()
    connection.close()
    
    return 'Record added successfully!'

if __name__ == '__main__':
    app.run(debug=True)

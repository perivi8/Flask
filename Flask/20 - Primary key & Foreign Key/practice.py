from flask import Flask, request, render_template , redirect , url_for , jsonify
import pyodbc

app = Flask(__name__)


# Database connection
def get_db_connection():
    connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=DESKTOP-6KV2EF8;"
                          "Database=practice1;"
                          "Trusted_Connection=yes;")
    return connection

@app.route('/')
def home():
    return render_template('show.html')


@app.route('/region')
def region():
    return render_template('practice.html')

@app.route('/add_region', methods=['POST'])
def add_region():
    region_id = request.form['region_id']
    region_description = request.form['region_description']

    try :           # Note 1 :-  For PRIMARY KEY error
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO region VALUES (?, ? )", (region_id , region_description))
        connection.commit()
    
        return jsonify({"message": "Region added successfully"}), 201
    
    except :         # Note 1 :-  For PRIMARY KEY error
        return ({'message' : 'Already ID was EXIST'})




@app.route('/territory')
def territory():
    return render_template('practice1.html')


@app.route('/add_territory', methods=['POST'])
def add_territory():
    territory_id = request.form['territory_id']
    territory_description = request.form['territory_description']
    region_id = request.form['region_id']

    try :              # Note 1 :-  For FOREIGN KEY error
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Territories VALUES (?, ? , ? )", (territory_id , territory_description , region_id))
        connection.commit()

        return jsonify({"message": "Territory added successfully"}), 201
    
    except :           # Note 1 :-  For FOREIGN KEY error
        return ({'message' : 'Region_ID  is not Belongs to "FOREIGN KEY " "or" "Territory_Id already Exists" '})




@app.route('/update')
def update():
    return render_template('practice2.html')

@app.route('/update_territory', methods=['POST'])
def update_territory():

    try :              # Note 1 :-  For FOREIGN KEY error

        territory_description = request.form['territory_description']
        region_id = request.form['region_id']
        territory_id = request.form['territory_id']

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("UPDATE Territories SET regionID = ? , territorydescription = ?   WHERE territoryID = ?", (region_id, territory_description ,territory_id))

        if cursor.rowcount == 0:   
            return jsonify({'error': 'Territory_ID  is an - Not an Existing ID'}), 404
        
        connection.commit()

        return jsonify({"message": "Territory updated successfully"}), 200

    except:              # Note 1 :-  For FOREIGN KEY error
        return ({'message' : 'Region_ID is not Belongs to "FOREIGN KEY " '})
    


if __name__ == '__main__':
    app.run(debug=True)




# Note 1 :- 

# Just use the  [ try : , except : method ] for showimg PRIMARY KEY , FOREIGN KEY errors 

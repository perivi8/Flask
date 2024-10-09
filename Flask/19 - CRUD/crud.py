import pandas as pd

import pyodbc

from flask import jsonify , Flask , request , render_template , redirect , url_for

app = Flask(__name__)

Driver="{ODBC Driver 17 for SQL Server};"
Server="DESKTOP-6KV2EF8;"
Database="bajaj;"
Trusted_Connection="yes;"


try :

    connection = pyodbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection={Trusted_Connection};')
    cursor = connection.cursor()

    df = cursor.execute('select * from employee')

except pyodbc.Error as er :

    print(f"Error connecting your SQL server : {er}")


# Show the DATA
@app.route('/')
def show():
    return render_template("home.html" , content = df)


@app.route('/getdata')
def getdata():       
        cursor.execute('select * from employee')
        list = cursor.fetchall()

        data = []
        for i in list :
            rows = {'emp_id' : i[0] ,"emp_name" : i[1] , "age":i[2] , "city" : i[3]}
            data.append(rows)

        print(data)

        return jsonify({"data" : data})


# INSERT DATA
@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/insert' , methods=['POST'] )
def insert():
    emp_id = request.form['emp_id']
    emp_name = request.form['emp_name']
    age = request.form['age']
    city = request.form['city']
    
    try :
        connection = pyodbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection={Trusted_Connection};')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO employee VALUES (?, ? , ? ,?)", (emp_id, emp_name , age ,city))
        connection.commit()

        return redirect(url_for('getdata'))

    except :
        return ({'message' : 'Already ID was EXIST'})


# UPDATE
@app.route('/new')
def update():
    return render_template('update.html')


@app.route('/update', methods=['POST'])
def update_data():
    
    id = request.form['emp_id'] 
    name = request.form['emp_name']
    age = request.form['age']
    city = request.form['city']
     

    connection = pyodbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection={Trusted_Connection};')
    cursor = connection.cursor()

    cursor.execute("UPDATE employee SET emp_name = ? , age = ? , city = ?  WHERE emp_id = ?", (name, age ,city, id))

    # If we try to UPDATE not Existing DATA , then it show error
    if cursor.rowcount == 0:
        return jsonify({'error': 'Data not found'}), 404
    
    connection.commit()

    return redirect(url_for('getdata'))




# DELETE
@app.route('/remove')
def remove():
    return render_template('delete.html')


@app.route('/delete', methods=['POST'])
def delete_data():
    emp_id = request.form['emp_id']
  
    connection = pyodbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Trusted_Connection={Trusted_Connection};')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM employee WHERE emp_id = ?', (emp_id,))

     # If we try to DELETE not Existing DATA , then it show error
    if cursor.rowcount == 0:
        return jsonify({'error': 'Data not found'}), 404
    
    connection.commit()

    return redirect(url_for('getdata'))




if __name__ == '__main__' :
    app.run(host="localhost" , port=5001 , debug=True)


































# Creating Table

# @app.route('/create')
# def create () :
#     create_table = ''' CREATE TABLE product ( product_id int primary key identity , product_name nvarchar(50), price int ) '''
#     cursor.execute(create_table)
#     connection.commit()


# INSERT Data to Table

# @app.route('/insert')
# def insert () :
#     Insert_data = ''' insert into employee values (3 , 'vinit' , 24 , 'nellore') '''
#     cursor.execute(insert_data)
#     connection.commit()


# UPDATE

# @app.route('/update')
# def update():    
#    update_query = ''' UPDATE employee SET age = 22 WHERE emp_id = 6 '''
#    cursor.execute(update_query)
#    connection.commit()
#    return "update sucessfull"


# DELETE

# @app.route('/delete')
# def delete(): 
#     delete_data = ''' delete from employee where emp_id = 5 '''
#     cursor.execute(delete_data)
#     connection.commit()
#     return "Delete sucessfull"
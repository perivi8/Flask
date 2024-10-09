#  GET , POST

from flask import Flask , render_template , redirect , url_for , request , jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("final.html")


@app.route('/login', methods = ['GET'])
def getmethod():
    name = request.args['name']
    email = request.args['email']
    return render_template("final1.html" , Name = name  , Email = email)



@app.route('/password' , methods = ['POST'])
def password():
    password = request.form['password']
    return ({"password" : password})


if __name__ == '__main__' :
    app.run(debug=True , port=4001)
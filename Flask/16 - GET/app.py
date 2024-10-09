#  GET

#  In GET method the Enter data show in URL

#  Referral link :- https://media.geeksforgeeks.org/wp-content/uploads/20230108193254/My-Project.gif

from flask import Flask , render_template , redirect , url_for , request , jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("admin.html")

@app.route('/login', methods = ['GET'])
def getmethod():
    name = request.args['name']
    email = request.args['email']

    return render_template('admin.html' , Name = name , Email = email)


if __name__ == '__main__' :
    app.run(debug=True , port=4001)
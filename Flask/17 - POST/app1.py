# POST

#  It will not show the data in URL

# Reference Link :- https://media.geeksforgeeks.org/wp-content/uploads/20230108193254/My-Project.gif

from flask import Flask , render_template , redirect , url_for , request , jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("admin1.html")


@app.route('/send' , methods = ['POST'])
def postmethod():
    name = request.form['name']
    email = request.form['email']

    return  render_template('admin1.html' , Name = name , Email = email)


if __name__ == '__main__' :
    app.run(debug=True , port=5001)
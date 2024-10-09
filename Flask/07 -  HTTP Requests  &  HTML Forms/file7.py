# HTTP Requests & HTML Forms


from flask import Flask , render_template , redirect , url_for , request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login' ,  methods = ['POST' , 'GET'])  # Must write in CAPITAL letters only ( POST , GET )
def login():

    if request.method == 'POST':                    # Must write in capital letters only (POST)
        user_name = request.form['usr_name']        
        return redirect(url_for("user" , usr = user_name))  
     
    return render_template("login.html")


@app.route('/<usr>')
def user(usr):
    return f'hlo - {usr} !'

if __name__ == "__main__":
    app.run(debug=True)
#  Flask Sessions

from flask import Flask , render_template , redirect , url_for , request , session

app = Flask(__name__)
app.secret_key = "hari_tutorial"                    # Note 1




@app.route('/')
def home():
    return render_template("home.html")




@app.route('/login' ,  methods = ['POST' , 'GET']) 
def login():

    if request.method == 'POST':                      
        user_name = request.form['usr_name'] 
        session['users'] = user_name                 # Note 2
        return redirect(url_for("user"))             # Note 3
    
    else:                                            # Note 9 -- last point
      if 'users' in session:
          return redirect(url_for('user'))
      
    return render_template("login.html")




@app.route('/user')                                  
def user():
    if 'users' in session:                           # Note 4
        user_name1 = session['users']
        return f'Hello Mr/Miss :- {user_name1}'
    else :                                           # Note 5
        return redirect(url_for('login'))




@app.route('/logout')                                # Note 6
def logout():
    session.pop("users" , None)                      # Note 7
    return redirect(url_for("login"))                # Note 8


if __name__ == "__main__":
    app.run(debug=True)






# NOTES 

# Reference Link :- https://youtu.be/RQM9mP4ZZZM?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6

# Note 1 :- Firest we need to create a ( SECERET KEY )

# Note 2 :- We need to create ( Session object ) , In this ['users'] = key , ( user_name ) is value / variable

# Note 3 :- After enter details in HTML page , it will redirect to ( /user ) URL

# Note 4 :- If the ( 'users' ) satisfy the ( session ) condition , then it will return the ( user_name1 )

# Note 5 :- If the ( 'users' )  does not satisfy the ( session ) condition , then it will return the ( login ) page.

# Note 6 :- If we want to remove the ( user ) details then we need to use ( /logout ) URL.

# Note 7 :- If we want to remove ( user ) details means use ( session.pop('users' , None) )

# Note 8 :- Ater remove the ( user ) details , then redirect to the ( /login ) URL

# Note 9 :- When we are trying to enter ( /login ) URL , without enter ( /logout ) URL  , then again it show ( user ) details.
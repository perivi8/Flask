#  

from flask import Flask , render_template , redirect , url_for , request , session

from datetime import timedelta   

from flask import flash

app = Flask(__name__)
app.secret_key = "hari_tutorial"    
app.permanent_session_lifetime = timedelta(minutes=5)        



@app.route('/')
def home():
    return render_template("user.html")


@app.route('/login' ,  methods = ['POST' , 'GET']) 
def login():

    if request.method == 'POST':  
        session.permanent = True                              
        user_name = request.form['usr_name'] 
        session['users'] = user_name   
        flash("Login Successful !!")                            # Note 1       
        return redirect(url_for("user"))           
    
    else:                                            
      if 'users' in session:
          flash("You are already logged in !!")                 # Note 2
          return redirect(url_for('user'))
      
    return render_template("login.html")


@app.route('/user' )                                  
def user():
    if 'users' in session:                           
        user_name1 = session['users']
        return render_template("user.html" , user=user_name1)
    else :      
        flash("you are not logged in!")                         # Note 3
        return redirect(url_for('login'))



@app.route('/logout')                              
def logout():
    session.pop("users" , None)    
    flash("You have been logged out!" , 'info')                 # Note 4
    return redirect(url_for("login"))                


if __name__ == "__main__":
    app.run(debug=True)





# NOTES 

# Note 1 :- If we give the login details , the flash message will appear in ( user.html ) page , Because the " login " page redirect to " user " page 

# Note 2 :- If we are already login , again we try to login means it show the flash message in ( user.html ) page , Because the " login " page redirect to " user " page 

# Note 3 :- With out "login" , we type ( /user ) URL , it will Flash the message in ( login.html ) , Because it redirect to " login " page

# Note 4 :- If we are given ( /logout ) URL means , it flash the message in ( login.html ) , Because it redirect to " login " page
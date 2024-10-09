#  Flask Sessions ( Set Time )

from flask import Flask , render_template , redirect , url_for , request , session

from datetime import timedelta                                # Note 1

app = Flask(__name__)
app.secret_key = "hari_tutorial"    
app.permanent_session_lifetime = timedelta(minutes=5)         # Note 2



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login' ,  methods = ['POST' , 'GET']) 
def login():

    if request.method == 'POST':  
        session.permanent = True                              # Note 3         
        user_name = request.form['usr_name'] 
        session['users'] = user_name                
        return redirect(url_for("user"))           
    
    else:                                            
      if 'users' in session:
          return redirect(url_for('user'))
      
    return render_template("login.html")


@app.route('/user')                                  
def user():
    if 'users' in session:                           
        user_name1 = session['users']
        return f'Hello Mr/Miss :- {user_name1}'
    else :                                           
        return redirect(url_for('login'))



@app.route('/logout')                              
def logout():
    session.pop("users" , None)                     
    return redirect(url_for("login"))                


if __name__ == "__main__":
    app.run(debug=True)






# NOTES 

# After we set the time , when we close the browser , and again open the browser also the Login status will show . It work only - till we given time   

# Reference Link :-(10:45) https://youtu.be/RQM9mP4ZZZM?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6



# Note 1 :- we need to import "timedelta" from "datetime"

# Note 2 :- we need to set the time ( i.e. "hours"  or  "minutes" ) 

# Note 3 :- without the ( session.permanent = True ) condition it will not work.
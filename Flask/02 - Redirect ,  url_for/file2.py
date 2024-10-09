#  Redirect ,  url_for


from flask import Flask , redirect , url_for

app = Flask(__name__)



@app.route('/')
def home():
    return "This is Default URL"


@app.route('/courses')
def list_of_courses():
    return "<h4>CSE</h4> <h4>ECE</h4> <h4>ME</h4> "


# Redirect

@app.route('/admin')
def method_name():
    return redirect('/') 


# url_for

@app.route('/admin1')
def adam():
    return redirect(url_for("list_of_courses")) 


if __name__ ==  '__main__':
    app.run(debug = True)



# NOTES


# Reference Link :- (10:16) https://youtu.be/7ZvXGNKwXp8?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6
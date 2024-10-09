#  Basics 

from flask import Flask

app = Flask(__name__)


@app.route("/")  # Note 1
def home():
    return "<h1>Hello World !"


@app.route('/courses')  # Note 2
def courses_list():
    return "<h4>Telugu</h4><h4>Hindi</h4><h4>English</h4>"


@app.route('/<name>')  # Note 3 ( Dynamic Routing )
def method_name(name):
    return f"hii :- {name}"



if __name__ == '__main__':
    app.run(debug = True)  # Note 4



 

# NOTES


# Note 1 :- '/' it is Default

# Note 2 :- We need to write this in after URL in website 

# Note 3 :- We need to mention Same ' name '  in Below Parameters also , we can change any "word" in place of 'name'

# Note 4 :- If we not mention ( debug = True ), we need to run code in Terminal  every time after update in VScode

# Referral Link :- https://youtu.be/7ZvXGNKwXp8?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6
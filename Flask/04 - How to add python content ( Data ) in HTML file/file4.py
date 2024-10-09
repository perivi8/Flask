# How to add python content ( Data ) in HTML file


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html' , content = "Flask Tutorial")

if __name__ == '__main__':
    app.run(debug=True)



#  Reference Link :- (6:39) https://youtu.be/YWh3IRVR_74?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6

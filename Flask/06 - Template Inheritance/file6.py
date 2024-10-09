# Template Inheritance 

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def inheritance1():
    return render_template("inheritance1.html")


@app.route('/krishna')
def inheritance2():
    return render_template("inheritance2.html")


@app.route('/perivi')
def inheritance3():
    return render_template("inheritance3.html")


if __name__ == "__main__":
    app.run(debug=True)



#  Reference Link :- https://youtu.be/yn_gEelAERU?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6
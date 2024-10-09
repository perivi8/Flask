# How to write Python ' for loop ' & ' If condition ' in HTML file


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html' , content = ['ML' , 'DL' , 'python' , 'HTML' , 'CSS' , "JS" , 'SQL' ,'FLASK'])



if __name__ == '__main__':
    app.run(debug=True)



# Reference Link :- (8:25) https://youtu.be/YWh3IRVR_74?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6
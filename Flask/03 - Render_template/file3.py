# Render_template

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gym.html')

if __name__ == '__main__':
    app.run(debug=True)






# NOTES

# Compulasry we need to create a folder ( templates ) , in this folder we need to create HTML file

# Reference link :- https://youtu.be/YWh3IRVR_74?list=PLVG0Zju2HPJdIoMidf1i0hfccIcsGTyx6

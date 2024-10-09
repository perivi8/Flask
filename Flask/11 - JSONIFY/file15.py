from flask import Flask  , jsonify

app = Flask(__name__)


@app.route('/')
def with_jsonfy():
    list1 = [
        {
            "name" : "hari" ,
            "age" : 23 ,
            "department" : " ECE"
        }
    ]
    return jsonify(list1)



@app.route('/list2')
def without_jsonfy():
    list2 = {
        "name" : "perivi" ,
        "age" : 25 ,
        "department" : " CSE"
    }
    return list2



if __name__ == '__main__' :
    app.run(debug=True)
    


#  NOTES

# If the " FLASK vesrion is 1.1.0 " or " more "  means no need to " mention jsonfy "
from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        "Contact":"9987644456",
        "Name":"Raju",
        "done":False,
        "id": 1
    },
    {
        "Contact":"9987644879",
        "Name":"Rani",
        "done":False,
        "id": 2
    }
]

@app.route("/")
def hello():
    return "Hello!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    data= {
        'id': data[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    data.append(data)
    return jsonify({
        "status":"success",
        "message": "data added succesfully!"
    })
    

@app.route("/get-data")
def get_data():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
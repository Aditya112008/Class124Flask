from logging import debug
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO WORLD !" 

tasks = [
    {
        'id':1,
        'title': u'buy groceries',
        'description':u'milk,cheese,butter,fruits',
        'done': False
    },
    {
        'id':2,
        'title': u'learn python',
        'description':u'need to find a good python tutorial',
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })



@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks 
    })







if(__name__ == "__main__"):
    app.run(debug = True)           
    app.run() 


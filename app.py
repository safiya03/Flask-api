from flask import Flask, jsonify, request, make_response


app = Flask(__name__)

tasks = [
    {
        'id': 0,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 1,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def index():
    if request.authorization and request.authorization.username =='username' and request.authorization.password == 'password':
        return 'You are logged in'
    
    return make_response('Could not verify your login!',401,{'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/tasks', methods=['GET'])
def get():
    return jsonify({'Tasks':tasks})

@app.route('/tasks/<int:tasks_id>', methods = ['GET'])
def get_task(tasks_id):
    return jsonify({'tasks':tasks[tasks_id]})

@app.route('/tasks', methods = ['POST'])
def create():
    tasks={
        'id': 2,
        'title': u'Driving',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False}





if __name__ == "__main__":
    app.run()
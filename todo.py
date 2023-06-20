from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
# db connection
client = MongoClient('mongodb://localhost:27017/')
db = client['todo_list']
collection = db['tasks']

# home route
@app.route('/')
def index():
    tasks = collection.find()
    return render_template('index.html', tasks=tasks)

# add task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    collection.insert_one({'task': task})
    return redirect('/')

# delete task
@app.route('/delete', methods=['POST'])
def delete():
    task = request.form['dtask']
    collection.delete_one({'task': task})
    return redirect('/')

# host
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3000',debug=True)


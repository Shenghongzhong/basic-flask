from flask import Flask
from flask import request, jsonify
from data import *

app = Flask(__name__)
app.config['DEBUG'] = True

# Create  test data



@app.route("/",methods = ['GET'])
def home():
    return '''
    <h1>Distant Reading Archive</h1>
    <p> This site is a prototype API for distant reading of science fiction novels.</p>'''

@app.route("/api/v1/resources/books/all",methods=['GET'])
def api_all():
    return jsonify(books)

@app.route("/api/v1/resources/books",methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)
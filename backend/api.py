from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def index():
    list = [{'id': 1, 'username': 'test1'}]
    return jsonify({'response': list})

@app.route('/post', methods=['POST'])
def index2():
    data = request.get_json()
    print(data)
    return data

if __name__ == "__main__":
    app.run(debug=True)
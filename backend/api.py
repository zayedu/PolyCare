from flask import Flask, jsonify, request
from flask_cors import CORS

from uploadResults.discussSymptoms import discussSymptoms
from uploadResults.discussBloodTest import discussBloodTest

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def index():
    list = [{'id': 1, 'username': 'test1'}]
    return jsonify({'response': list})

@app.route('/SymptomUploadResults', methods=['POST'])
def SymptomUploadResults():

    incomingReq = request.get_json()
    uploadsymptoms = discussSymptoms(incomingReq).uploadUserSymptom()

    return uploadsymptoms 

@app.route('/BloodTestUploadResults', methods=['POST'])
def BloodTestUploadResults():

    incomingReq = request.get_json()
    uploadblood = discussBloodTest(incomingReq).uploadUserBloodTest()

    return uploadblood

if __name__ == "__main__":
    app.run(debug=True)
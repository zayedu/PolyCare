from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from uploadResults.discussUltrasound import discussUltrasound
from uploadResults.discussSymptoms import discussSymptoms
from uploadResults.discussBloodTest import discussBloodTest

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    users = [{'id': 1, 'username': 'test1'}]
    return jsonify({'response': users})

@app.route('/SymptomUploadResults', methods=['POST'])
@cross_origin()
def SymptomUploadResults():
    incomingReq = request.get_json()
    result = discussSymptoms(incomingReq).uploadUserSymptom()
    # Wrap the result in a proper response; if result is already a JSON string,
    # we set its Content-Type accordingly.
    response = make_response(result)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/UltrasoundAnalyzer/UploadResults', methods=['POST'])
@cross_origin()
def UltrasoundUploadResults():
    result = discussUltrasound(request).uploadUltrasound()
    response = make_response(result)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/BloodTestUploadResults', methods=['POST'])
def BloodTestUploadResults():

    incomingReq = request.get_json()
    uploadblood = discussBloodTest(incomingReq).uploadUserBloodTest()

    return uploadblood

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from uploadResults.discussUltrasound import discussUltrasound
from backend.uploadResults.discussSymptoms import discussSymptoms

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

@app.route('/UltrasoundAnalyzer/UploadResults', methods=['POST'])
def UltrasoundUploadResults():

    uploadUltrasound = discussUltrasound(request).uploadUltrasound()


    return uploadUltrasound

if __name__ == "__main__":
    app.run(debug=True)
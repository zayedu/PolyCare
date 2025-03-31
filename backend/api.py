from flask import Flask, jsonify, request
from flask_cors import CORS
from results_viewer_service import ResultsViewerService

from uploadResults.discussSymptoms import discussSymptoms

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

@app.route("/api/getResults", methods=["GET"])
def get_results():
    """
    Returns the four scores, plus recommendation and lifestyle tips, in JSON format.
    If no results exist, returns {"success": False, "message": "No results found"}.
    """
    rvs = ResultsViewerService()
    results_data = rvs.get_results_and_recommendation()
    return jsonify(results_data)

if __name__ == "__main__":
    app.run(debug=True)
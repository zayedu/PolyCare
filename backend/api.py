from flask import Flask, jsonify, request
from flask_cors import CORS
from likelihood_calculation_service import LikelihoodCalculationService
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

@app.route("/api/calculateLikelihood", methods=["POST"])
def calculate_likelihood():
    # Create a new instance of the service
    lcs = LikelihoodCalculationService()
    # Retrieve individual scores
    symp_score = lcs.get_symptoms_score()
    bt_score = lcs.get_blood_test_score()
    us_score = lcs.get_ultrasound_score()
    # Calculate overall likelihood
    overall_score = lcs.receive_overall_score(symp_score, bt_score, us_score)
    # Save the results to the "database"
    lcs.sendToDB(overall_score, symp_score, bt_score, us_score)
    return jsonify({"success": True, "message": "Likelihood calculated and stored."}) 

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
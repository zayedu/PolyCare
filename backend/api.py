from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from account_system.account_login import AccountLogin
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
@cross_origin()
def BloodTestUploadResults():

    incomingReq = request.get_json()
    uploadblood = discussBloodTest(incomingReq).uploadUserBloodTest()

    return uploadblood

@app.route("/api/calculateLikelihood", methods=["POST"])
@cross_origin()
def calculate_likelihood():
    from calculateResults.likelihood_calculation_service import LikelihoodCalculationService
    
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
@cross_origin()
def get_results():
    """
    Returns the four scores, plus recommendation and lifestyle tips, in JSON format.
    If no results exist, returns {"success": False, "message": "No results found"}.
    """
    from results_viewer_service import ResultsViewerService
    rvs = ResultsViewerService()
    results_data = rvs.get_results_and_recommendation()
    return jsonify(results_data)

@app.route('/LoginAttempt', methods=['POST'])
@cross_origin()
def LoginAttempt():

    # Validate credentials 
    user = AccountLogin('Sfwre12', '3rdYear!')
    result = user.login()
    
    message = {"Test": result}
    return message

if __name__ == "__main__":
    app.run(debug=True)

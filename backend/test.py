

from flask import json
from calculateResults.symptomCalculation import symptomCalculation
from backend.uploadResults.discussSymptoms import discussSymptoms

# Test to upload data into uploadData.csv
discussSymptoms(json.dumps({"test": "random data input"})).uploadUserSymptom()

# Test to retreive data from uploadData.csv
print(symptomCalculation().getUserSymptoms())

# Test for calculating PCOS based off data stored in uploadData.csv
print("Probablity: ",symptomCalculation().calculatePCOSFromSymptom())

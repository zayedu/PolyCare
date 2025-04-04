

from flask import json
from calculateResults.bloodCalculation import bloodCalculation
# from calculateResults.symptomCalculation import symptomCalculation
# from calculateResults.UltrasoundCalculation import UltrasoundCalculation

#from calculateResults.UltrasoundCalculation import UltrasoundCalculation

# Test to upload data into uploadData.csv
# discussSymptoms(json.dumps({'response': ['Yes a lot', 'Yes everywhere', 'Oily skin always', 'Yes it is very hard', 'Kind of']})).uploadUserSymptom()

# Test to retreive data from uploadData.csv
#print(symptomCalculation().getUserSymptoms())

# Test for calculating PCOS based off data stored in uploadData.csv
#print("Probablity: ",symptomCalculation().calculatePCOSFromSymptom())

# assume image stored in db already
# ultrasoundCalculation = UltrasoundCalculation()
# result = ultrasoundCalculation.predict()
# print(result)

# Test for calculating PCOS based off data stored in uploadData.csv
print("Probablity: ",bloodCalculation().runProbability())
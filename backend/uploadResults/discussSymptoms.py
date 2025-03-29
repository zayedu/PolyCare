from flask import json
import csv

class discussSymptoms():
    def __init__(self, data:json):
        self.data = data

    def uploadUserSymptom(self):

        # Can remove after testing
        print(self.data)
        
        # TODO: actually parse request data into an array
        sampleData= ['Not really', 'Only a bit in the back', 'Yes acne has been there', 'Have witnessed unexpected weight gain', 'Yes little']

        with open('data/uploadedData.csv', 'r+') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(sampleData)

        message = json.dumps({"response": "Succesfully uploaded data"})
        
        return message
    
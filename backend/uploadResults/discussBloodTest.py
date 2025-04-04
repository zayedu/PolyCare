from flask import json
import csv

import pandas as pd

class discussBloodTest():
    """
    Description: Initializes 'discuss bloodtest' instance
    """
    def __init__(self, incomingReq:json):
        self.incomingReq = incomingReq

    def uploadUserBloodTest(self):
        """
        Description: Upload's user symptom to data base
        Args: None
        Requires: N/A
        Modifies: uploadedData.csv
        Returns: success message as a json response to front end
        """

        # Get blood test results as a list from request
        bloodTestData = self.parseRequest(self.incomingReq)

        # Currently hard coded to append data to uploadedData.csv

        # Load the CSV file
        csv_path = 'data/uploadedData.csv'
        df = pd.read_csv(csv_path)

        # Ensure there's at least one row to modify
        if df.empty:
            return json.dumps({"error": "CSV file is empty. Cannot update data."})

        # Update the first row of the 'Blood Test' columns
        df.at[0, 'Blood Test 1'] = bloodTestData[0]
        df.at[0, 'Blood Test 2'] = bloodTestData[1]
        df.at[0, 'Blood Test 3'] = bloodTestData[2]

        # Save the updated CSV
        df.to_csv(csv_path, index=False)

        # After uploading data, create a message to notify front end (user)
        message = json.dumps({"response": "Successfully uploaded data"})
        return message
    
    def parseRequest(self, incomingReq:json):

        # Parse request data into an array
        glucose = incomingReq['glucose']
        testosterone = incomingReq['testosterone']
        bileSalts = incomingReq['bileSalts']

        sampleData = [glucose, testosterone, bileSalts]
        # print(sampleData)
        return sampleData


    
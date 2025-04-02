from flask import json
import csv

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

        # Get symptoms as a list from request
        bloodTestData = self.parseRequest(self.incomingReq)

        # Currently hard coded to append data to uploadedData.csv
        # NOTE: Expect first row of uploadedData.csv to be column names
        # NOTE: Expect second row of uploadedData.csv to be blank line to write in row
        # NOTE: After running this method, will need to clear uploadedData.csv to above expectations
        with open('data/uploadedData.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(bloodTestData)

        # After uploading data, create a message to notify front end (user)
        message = json.dumps({"response": "Succesfully uploaded data"})
        
        return message
    
    def parseRequest(self, incomingReq:json):
        """
        Description: Parse's incoming request to get list of symptoms from user
        Args: incomingReq:json
        Requires: N/A
        Modifies: N/A
        Returns: 5 Symptoms inputted from user as a list
        """

        # Parse request data into an array
        
        glucose = incomingReq['glucose']
        testosterone = incomingReq['testosterone']
        bileSalts = incomingReq['bileSalts']

        sampleData = ["", "", "", "", "", glucose, testosterone, bileSalts, ""]
        print(sampleData)
        return sampleData
    
        
        # return ["", "", "", "", "", glucose, testosterone, bileSalts, ""]


    
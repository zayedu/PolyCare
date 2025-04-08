import pandas as pd
from flask import json

class discussSymptoms():
    """
    Description: Initializes 'discuss symptoms' instance.
    Args: Incoming upload symptom's POST request as a JSON.
    Requires: POST request triggered from the front end.
    Modifies: data/uploadedData.csv – always updates row 0 for symptom columns.
    Returns: A JSON response indicating success.
    """
    def __init__(self, incomingReq: json):
        self.incomingReq = incomingReq

    def uploadUserSymptom(self):
        """
        Description: Updates the first row (row 0) of data/uploadedData.csv with user symptom data.
        The first 5 columns (assumed to be "Symptom 1" through "Symptom 5") will be updated.
        Returns: A JSON string indicating success.
        """
        # Get symptoms as a list from the request
        sampleData = self.parseRequest(self.incomingReq)

        csv_path = 'data/uploadedData.csv'
        # Define the expected symptom column names
        symptom_cols = ["Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5"]

        try:
            df = pd.read_csv(csv_path)
        except FileNotFoundError:
            # If file doesn't exist, create a new DataFrame with required columns
            # Here we assume other columns exist as well but initialize them empty.
            columns = ["Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5",
                       "Blood Test 1", "Blood Test 2", "Blood Test 3", "Ultrasound Image"]
            df = pd.DataFrame(columns=columns)

        if df.empty:
            # Create a new row dictionary with all columns initialized to empty strings.
            new_row = {col: "" for col in df.columns}
            # Overwrite the symptom columns with sample data
            for i, col in enumerate(symptom_cols):
                new_row[col] = sampleData[i] if i < len(sampleData) else ""
            # Create a new DataFrame with that single row
            df = pd.DataFrame([new_row])
        else:
            # Overwrite row 0 in the symptom columns with sampleData
            for i, col in enumerate(symptom_cols):
                df.loc[0, col] = sampleData[i] if i < len(sampleData) else ""

        # Write the updated DataFrame back to the CSV, overwriting its contents.
        df.to_csv(csv_path, index=False)

        message = json.dumps({"response": "Successfully uploaded data"})
        return message

    def parseRequest(self, incomingReq: json):
        """
        Description: Parses the incoming JSON request to extract the list of symptom responses.
        Expects the request to have a key 'response' with a list of 5 symptom responses.
        Returns: List of symptom responses.
        """
        sampleData = incomingReq['response']
        return sampleData




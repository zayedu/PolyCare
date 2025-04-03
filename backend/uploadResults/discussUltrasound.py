from flask import json
import pandas as pd
import base64


class discussUltrasound():
    """
    Description: Initializes 'discuss symptoms' instance
    Args: Incoming upload symptom's post request as a json
    Requires: post request triggered from front end
    Modifies: NA
    Returns: NA
    """
    def __init__(self, incomingReq:json):
        self.image = incomingReq.files['image']

    def uploadUltrasound(self):
        """
        Description: Uploads user's symptom to the database.
        Args: None
        Requires: N/A
        Modifies: uploadedData.csv
        Returns: success/error message as a JSON response to the front end.
        """
        try:
            # Load the CSV file
            csv_path = 'data/uploadedData.csv'
            df = pd.read_csv(csv_path)

            # Ensure there's at least one row to modify
            if df.empty:
                return json.dumps({"error": "CSV file is empty. Cannot update data."})

            # Read and encode the image
            image_bytes = self.image.read()
            encoded_string = base64.b64encode(image_bytes).decode("utf-8")

            # Update the first row of the 'Ultrasound Image' column
            df.at[0, 'Ultrasound Image'] = encoded_string

            # Save the updated CSV
            df.to_csv(csv_path, index=False)

            # Success message
            message = json.dumps({"response": "Successfully uploaded data"})
            return message

        except FileNotFoundError:
            return json.dumps({"error": "CSV file not found. Ensure 'uploadedData.csv' exists."})

        except KeyError:
            return json.dumps({"error": "CSV file does not contain the 'Ultrasound Image' column."})

        except Exception as e:
            return json.dumps({"error": f"An unexpected error occurred: {str(e)}"})

    def parseRequest(self, incomingReq:json):
        """
        Description: Parse's incoming request to get list of symptoms from user
        Args: incomingReq:json
        Requires: N/A
        Modifies: N/A
        Returns: 5 Symptoms inputted from user as a list
        """
        print("Symptom upload request: ", self.incomingReq)
        sampleData =[]

        # TODO: actually parse request data into an array
        sampleData = ['Yes a lot', 'Only a bit in the back', 'Yes acne has been there and not going away', 'Have witnessed unexpected weight gain', 'Yes very much']

        return sampleData

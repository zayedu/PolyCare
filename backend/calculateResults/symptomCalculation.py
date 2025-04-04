from flask import json
import csv, requests, config

class symptomCalculation():
    """
    Description: Initializes 'symptom calculation' instance
    Args: N/A
    Requires: expects user's symptoms in data base
    Modifies: promptTemplate.txt
    Returns: NA      
    """
    def __init__(self):
        self.userSymptoms = self.getUserSymptoms()

    def getUserSymptoms(self):
        """
        Description: gets user's symptoms from data base
        Args: N/A
        Requires: expects user's symptoms in data base
        Modifies: N/A
        Returns: List of 5 symptoms     
        """

        # NOTE: Harcoded to always return 2nd row of uploadedData.csv and assume first 5 columns are symptom responses
        with open('data/uploadedData.csv', 'r') as csvfile:
            csvfiletoList = list(csv.reader(csvfile))
            responseList = (csvfiletoList[1])

        return responseList

    def constructPrompt(self):
        """
        Description: Construct prompt to send to llm
        Args: N/A
        Requires: user symptoms list from getUserSymptoms method
        Modifies: promptTemplate.txt
        Returns: N/A  
        """
        # Get symptoms in ordered list (Answer 1 is 1st element in list, Answer 2 is 2nd element in list...)
        userSymptomsList = self.userSymptoms

        # Copy previous prompt from promptTemplate.txt and change only lines of the answers with current user symptoms from list 
        with open('data/promptTemplate.txt', 'r') as textFile:
            prompt = textFile.readlines()
            prompt[3] = "Answer 1: "+userSymptomsList[0]+"\n"
            prompt[6] = "Answer 2: "+userSymptomsList[1]+"\n"
            prompt[9] = "Answer 3: "+userSymptomsList[2]+"\n"
            prompt[12] = "Answer 4: "+userSymptomsList[3]+"\n"
            prompt[15] = "Answer 5: "+userSymptomsList[4]+"\n"

        # Set updated prompt back to promptTemplate.txt
        with open('data/promptTemplate.txt', 'w') as textFile:
            textFile.writelines(prompt)

    def calculatePCOSFromSymptom(self):
        """
        Description: Calculate PCOS from Llm 
        Args: N/A
        Requires: Updated prompt text file with current user's symptoms filled 
        Modifies: N/a
        Returns: PCOS calculation as a float percentage  
        """

        # Set api key and url to be used
        API_KEY = config.API_KEY
        API_URL = 'https://openrouter.ai/api/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        # Update prompt with the current user's data  
        self.constructPrompt()

        # store promptTemplate.txt as a string 
        with open('data/promptTemplate.txt', 'r') as promptFile:
            prompt = promptFile.read()

        # Specify llm model and input prompt string
        spec = {
            "model": "deepseek/deepseek-chat:free",
            "messages": [{"role": "user", "content": prompt}]
        }

        # Send post request to llm and store the response
        response = requests.post(API_URL, json=spec, headers=headers)

        if response.status_code == 200:
            # print("API Response:", response.json())
            
            # parse llm response to find final content
            outputResponse = self.parseLlmOutput(response.json())

            # make sure llm response is a numerical value and not other text
            if not str(outputResponse).isdigit():
                # print("Response was successful but did not provide just a numerical probability")
                return None
            else:
                # if response is solely numerical value then convert response to type float
                numericalProbability = float(outputResponse)
        
        else:
            # print("Failed. Status Code:", response.status_code)
            return None
        
        return numericalProbability
        
    def parseLlmOutput(self, apiResponse:json):
        # parse llm response to store actual response 
        outputResponse = dict(apiResponse)['choices'][0]['message']['content']
        return outputResponse
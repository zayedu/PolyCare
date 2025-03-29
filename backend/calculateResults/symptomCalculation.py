from flask import json
import csv

import requests

import config

class symptomCalculation():
    def __init__(self):
        self.userSymptoms = self.getUserSymptoms()

    def getUserSymptoms(self):
        with open('data/uploadedData.csv', 'r') as csvfile:
            csvfile = csv.reader(csvfile)
            responseList = (next(csvfile))

        return responseList

    def constructPrompt(self):
        userSymptomsList = self.userSymptoms
        with open('data/promptTemplate.txt', 'r') as textFile:
            prompt = textFile.readlines()
            prompt[3] = "Answer 1: "+userSymptomsList[0]+"\n"
            prompt[6] = "Answer 2: "+userSymptomsList[1]+"\n"
            prompt[9] = "Answer 3: "+userSymptomsList[2]+"\n"
            prompt[12] = "Answer 4: "+userSymptomsList[3]+"\n"
            prompt[15] = "Answer 5: "+userSymptomsList[4]+"\n"

        with open('data/promptTemplate.txt', 'w') as textFile:
            textFile.writelines(prompt)

    def calculatePCOSFromSymptom(self):
        API_KEY = config.API_KEY
        API_URL = 'https://openrouter.ai/api/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        self.constructPrompt()
        with open('data/promptTemplate.txt', 'r') as promptFile:
            prompt = promptFile.read()

        spec = {
            "model": "deepseek/deepseek-chat:free",
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(API_URL, json=spec, headers=headers)

        if response.status_code == 200:
            print("API Response:", response.json())
        else:
            print("Failed. Status Code:", response.status_code)

        #TODO: Parse llm output
        # return 
        
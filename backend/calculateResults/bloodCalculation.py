from pathlib import Path
from flask import json
import pandas as pd
import csv, requests, config

class bloodCalculation():
    """
    Description: does PCOS probability based on user inputted results
    """
    def __init__(self):
        self.userBloodTest = self.getUserBloodTest()

    def getUserBloodTest(self):
        """
        Description: reads latest blood test entry 
        """

        bloodTests = []

        # NOTE: Harcoded to always return 2nd row of uploadedData.csv and assume first 5 columns are symptom responses
        # with open('data/uploadedData.csv', 'r') as csvfile:
        #     row = list(csv.reader(csvfile))
        #     lastRow = row[-1]
        path_to_csv = Path(__file__).parent.parent / "data/uploadedData.csv"
        df = pd.read_csv(path_to_csv)

        bloodTest1 = df.get('Blood Test 1')[0]
        bloodTest2 = df.get('Blood Test 2')[0]
        bloodTest3 = df.get('Blood Test 3')[0]

        if bloodTest1 is None:
            raise ValueError("CSV file does not contain 'bloodTest1' column.")
        
        return{"glucose": float(bloodTest1), "testosterone": float(bloodTest2), "bileSalts": float(bloodTest3)}
        
    def calculatePCOSfromBT(self):
        glucose = self.userBloodTest["glucose"]
        testosterone = self.userBloodTest["testosterone"]
        bileSalts = self.userBloodTest["bileSalts"]

        if glucose < 7:
            riskG = 0
        else:
            riskG = ((glucose - 7.0)/3.0)*33.0
        if testosterone < 70:
            riskT = 0
        else:
            riskT = ((testosterone - 70.0)/30.0)*33.0
        if bileSalts < 1181.14:
            riskBS = 0
        else:
            riskBS = ((bileSalts - 1181.14)/300.0)*34.0
    
        riskTotal = round(min((riskG + riskT + riskBS), 100), 2)
        return riskTotal

    def runProbability(self):
        riskScore = self.calculatePCOSfromBT()
        print(f"\nPCOS Probability: {riskScore}%")
        return riskScore

    
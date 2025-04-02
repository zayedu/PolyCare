from flask import json
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

        # NOTE: Harcoded to always return 2nd row of uploadedData.csv and assume first 5 columns are symptom responses
        with open('data/uploadedData.csv', 'r') as csvfile:
            row = list(csv.reader(csvfile))
            lastRow = row[-1]
            return{"glucose": float(lastRow[0]), "testosterone": float(lastRow[1]), "bileSalts": float(lastRow[2])}


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
        print("User Blood Test Input:")
        print(f"- Glucose: {self.userBloodTest['glucose']} mmol/L")
        print(f"- Testosterone: {self.userBloodTest['testosterone']} ng/dL")
        print(f"- Bile Salts: {self.userBloodTest['bileSalts']} mmol/L")

        riskScore = self.calculatePCOSfromBT()
        print(f"\nPCOS Probability: {riskScore}%")

    
import pandas as pd
from pathlib import Path

class LikelihoodCalculationService:
    
    def __init__(self):
        self.symp_calc = symptomCalculation()
        self.bt_calc = bloodTestCalculation()
        self.us_calc = ultrasoundCalculation()
        self.overall_calc = OverallCalculation(symptom_weight=0.2, blood_test_weight=0.35, ultrasound_weight=0.45)

    def get_symptoms_score(self):
        return self.symp_calc.get_result()

    def get_blood_test_score(self):
        return self.bt_calc.get_result()

    def get_ultrasound_score(self):
        return self.us_calc.get_result()

    def receive_overall_score(self, symp_score, bt_score, us_score):
        return self.overall_calc.calculate_overall_probability(symp_score, bt_score, us_score)

    def sendToDB(self, overall_score, symp_score, bt_score, us_score):
        file_path = Path("path/to/excel.xlsx")

        if file_path.exists():
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["SymptomScore", "BloodTestScore", "UltrasoundScore", "OverallScore"])
            
        new_row = {
            "SymptomScore": symp_score,
            "BloodTestScore": bt_score,
            "UltrasoundScore": us_score,
            "OverallScore": overall_score
        }
        
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(file_path, index=False)

    def getFromDB(self):
        file_path = Path("path/to/mock_database.xlsx")
        if not file_path.exists():
            return []

        df = pd.read_excel(file_path)
        if df.empty:
            return []

        last_row = df.iloc[-1]
        return [
            last_row["SymptomScore"],
            last_row["BloodTestScore"],
            last_row["UltrasoundScore"],
            last_row["OverallScore"]
        ]
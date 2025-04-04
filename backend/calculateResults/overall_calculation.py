class OverallCalculation:
    
    def __init__(self, symptom_weight=0.2, blood_test_weight=0.35, ultrasound_weight=0.45):
        self.symptom_weight = symptom_weight
        self.blood_test_weight = blood_test_weight
        self.ultrasound_weight = ultrasound_weight
    
    def calculate_overall_probability(self, symptom_likelihood, blood_test_likelihood, ultrasound_likelihood):
        return ((symptom_likelihood * self.symptom_weight) + (blood_test_likelihood * self.blood_test_weight) + (ultrasound_likelihood * self.ultrasound_weight))

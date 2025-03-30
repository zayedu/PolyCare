class OverallCalculation:
    
    def __init__(self, symptom_weight=0.2, blood_test_weight=0.35, ultrasound_weight=0.45):
        self.symptom_weight = symptom_weight
        self.blood_test_weight = blood_test_weight
        self.ultrasound_weight = ultrasound_weight
        self.symptom_calculation = symptomCalculation()
        self.blood_test_calculation = bloodTestCalculation()
        self.ultrasound_calculation = ultrasoundCalculation()

    def calculate_overall_probability(self, symp_calc, bt_calc, us_calc):
        return (symp_calc.get_result() * self.symptom_weight + bt_calc.get_result() * self.blood_test_weight + us_calc.get_result() * self.ultrasound_weight)

    def get_results(self):
        overall_percentage = self.calculate_overall_probability(self.symptom_calculation, self.blood_test_calculation, self.ultrasound_calculation)
        return [overall_percentage, self.symptom_calculation.get_result(), self.blood_test_calculation.get_result(), self.ultrasound_calculation.get_result()]

from calculateResults.likelihood_calculation_service import LikelihoodCalculationService

class ResultsViewerService:
    def __init__(self):
        self.lcs = LikelihoodCalculationService()

    def get_results_and_recommendation(self):
        """
        1) Retrieve the four scores from the Excel "database".
        2) If empty, return an indicator that there are no results.
        3) If not empty, interpret the overall score, get physician recommendation,
           and gather lifestyle tips.
        4) Return a dictionary with everything needed by the frontend.
        """
        scores = self.lcs.getFromDB()  # [symp, blood, ultrasound, overall] or []
        if not scores:
            return {
                "success": False,
                "message": "No results found",
            }

        symptom_score, blood_test_score, ultrasound_score, overall_score = scores

        # Physician recommendation logic
        recommendation = self._get_physician_recommendation(overall_score)

        # Lifestyle tips for PCOS management - placeholder examples
        lifestyle_tips = [
            "Maintain a balanced diet rich in whole grains and lean proteins.",
            "Incorporate regular exercise (at least 30 minutes a day).",
            "Manage stress through mindfulness or therapy sessions.",
            "Stay hydrated and ensure adequate sleep each night."
        ]

        return {
            "success": True,
            "scores": {
                "symptomScore": float(symptom_score),
                "bloodTestScore": float(blood_test_score),
                "ultrasoundScore": float(ultrasound_score),
                "overallScore": float(overall_score),
                "recommendation": recommendation,
                "lifestyleTips": lifestyle_tips
            }
        }

    def _get_physician_recommendation(self, overall_score):
        """
        If overall score > 50%, strong recommendation to see a physician.
        If overall score == 50%, uncertain but still recommend a physician.
        If overall score < 50%, not at high risk, but see physician if concerned.
        """
        if overall_score > 50:
            return "There is a high likelihood of PCOS. Please schedule a physician appointment."
        elif overall_score == 50:
            return ("The results are uncertain. You should still consider seeing a physician, "
                    "as there is a possibility of PCOS.")
        else:
            return ("You do not appear to be at high risk based on these results, but if you have "
                    "persistent concerns, you should still see a physician.")

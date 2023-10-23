from resources.learning_modules import Learning_Modules
from utils.utils import Utils

class ProgressTracker:
    def __init__(self):
        self.learning_modules = Learning_Modules()
        self.quiz_scores = [{'score': 0, 'score_display': "Not Completed!"} for _ in range(len(self.learning_modules.levels))]
        # self.challenge_scores = [{'score': 0, 'score_display': "Not Completed!"} for _ in range(len(self.learning_modules.levels))]
        self.challenge_scores = []
        for level in self.learning_modules.levels:
            if level.challenge is not None:
                self.challenge_scores.append({'score': 0, 'score_display': "Not Completed!"})
    
    def update_quiz_score(self, level, new_score, num_of_questions):
        score_to_be_updated = self.quiz_scores[level - 1]
        score_to_be_updated['score'] = new_score
        score_to_be_updated['score_display'] = f"{new_score}/{num_of_questions}"

    def update_challenge_score(self, level, new_score, num_of_questions):
        score_to_be_updated = self.challenge_scores[level - 1]
        score_to_be_updated['score'] = new_score
        score_to_be_updated['score_display'] = f"{new_score}/{num_of_questions}"

    def display_progress(self):
        for i in range(len(self.quiz_scores)):
            Utils.display_str(f"Level {i + 1}")
            print(f"Quiz {i + 1}: {self.quiz_scores[i]['score_display']}")
            if len(self.challenge_scores) - 1>= i :
                print(f"Challenge {i + 1}: {self.challenge_scores[i]['score_display']}")
        print("")

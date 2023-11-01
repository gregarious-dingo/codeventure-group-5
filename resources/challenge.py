class Challenge:
    def __init__(self, challenges=None):
        self.challenges = challenges

    # def start(self, level, learner):
    #     score = 0
    #     if self.challenges is not None:
    #         for i, challenge in enumerate(self.challenges, start = 1):
    #             print(f"Challenge {i}: {challenge['question']}\n")

    #             user_ans = input("Answer (pay attention to code format and avoid unnecessary spaces!): ")
    #             if challenge['correct_answer'] == user_ans:
    #                 print("Correct!\n")
    #                 score += 1
    #             else:
    #                 print("Incorrect!\n")
        
    #     num_of_questions = len(self.challenges)
    #     learner.progress_tracker.update_challenge_score(level.level, score, num_of_questions)
    #     print(f'You have completed the "{level.name}" challenge and your score is: {score}/{num_of_questions}')

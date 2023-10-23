class Quiz:
    def __init__(self, quiz_questions):
        self.quiz_questions = quiz_questions

    def __len__(self):
        return len(self.quiz_questions)

    def start(self, level, learner):
        score = 0
        print("Quiz:")
        for i, question in enumerate(self.quiz_questions, start = 1):
            print(f"Question {i}: {question['question']}\n")
            for j, option in enumerate(question['options'], start = 1):
                print(f"{j}. {option}")

            user_ans = int(input("Answer (enter the option number): "))

            while not 1 <= user_ans <= len(question['options']):
                Utils.display_str("Please enter a valid option number")
                for j, option in enumerate(question['options'], start = 1):
                    print(f"{j}. {option}")
                user_ans = int(input("Answer (enter the option number): "))

            if question['correct_answer'] == user_ans:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect!\n")

        num_of_questions = len(self.quiz_questions)
        learner.progress_tracker.update_quiz_score(level.level, score, num_of_questions)
        print(f'You have completed the "{level.name}" quiz and your score is: {score}/{num_of_questions}')


import tkinter as tk
from challenge_frame import ChallengeFrame

class QuizFrame(tk.Frame):
    def __init__(self, master, modules_frame, level, question_index, quiz_score, user, learner_answers=[]):
        super().__init__(master)
        self.modules_frame = modules_frame
        self.level = level
        self.question_index = question_index
        self.user = user
        self.quiz = level.quiz
        self.quiz_score = quiz_score
        self.learner_answers = learner_answers

        if question_index != len(self.quiz):
            self.quiz_question = self.quiz.quiz_questions[question_index]

            quiz_name_message = tk.Label(self, text=f"{self.quiz_question['question']} \n\n\n\nPick a correct answer:")
            quiz_name_message.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky=tk.N)

            self.answer = tk.StringVar()
            row = 1
            for i, option in enumerate(self.quiz_question["options"]):
                self.answer_button = tk.Radiobutton(self,
                                                    text=option,
                                                    variable=self.answer,
                                                    value=i + 1,
                                                    command="")
                self.answer_button.grid(row=row, column=1, sticky=tk.W)

                row += 1

            submit_button = tk.Button(self, text="Submit", command=self.submit)
            submit_button.grid(row=row + 3, columnspan=2, pady=50)

        else:
            # Move to challenge frame
            num_of_question = len(self.quiz)
            self.user.progress_tracker.update_quiz_score(self.level.level, self.quiz_score, num_of_question)
            self.show_quiz_result()

    def next_question(self):
        self.place_forget()
        next_question_frame = QuizFrame(self.master,
                                        self.modules_frame,
                                        self.level,
                                        self.question_index + 1,
                                        self.quiz_score,
                                        self.user,
                                        self.learner_answers)
        next_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_quiz_result(self):
        self.place_forget()
        quiz_result_frame = QuizResultFrame(self.master,
                                            self.modules_frame,
                                            self.level,
                                            self.learner_answers,
                                            self.quiz_score,
                                            self.user)
        quiz_result_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def submit(self):
        answer = self.answer.get()
        self.learner_answers.append(answer)

        if answer:
            if int(answer) == self.quiz_question['correct_answer']:
                # Update progress tracker. Score increment by 1
                self.quiz_score += 1
                self.next_question()
            else:
                self.next_question()
        else:
            level_name_message = tk.Label(self, text="Please select an answer.")
            level_name_message.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)


class QuizResultFrame(tk.Frame):
    def __init__(self, master, modules_frame, level, learner_answers, quiz_score, user):
        super().__init__(master)
        self.modules_frame = modules_frame
        self.level = level
        self.quiz = self.level.quiz
        self.learner_answers = learner_answers
        self.quiz_score = quiz_score
        self.user = user


        quiz_result_message = tk.Label(self,
                                       text="Your quiz results:",
                                       font=("Arial Bold", 20))
        quiz_result_message.pack()

        row=2
        quiz_num = 1
        answer_index = 0
        for question in self.quiz.quiz_questions:
            if int(self.learner_answers[answer_index]) == question['correct_answer']:
                quiz = tk.Label(self, text=f"Quiz question {quiz_num}: {question['question']} ✔", bg = "green")
                quiz.pack()

            else:
                quiz = tk.Label(self, text=f"Quiz question {quiz_num}: {question['question']} ✘", bg="red")
                quiz.pack()

            quiz_answer_comparison = tk.Label(self,
                                              text=f"Your answer: {self.learner_answers[answer_index]}\n" 
                                              +f"Correct answer: {question['correct_answer']}")
            quiz_answer_comparison.pack()
            
            row += 1
            quiz_num += 1
            answer_index += 1

    
        next_button = tk.Button(self,
                                             text="Next",
                                             command=self.next)
        next_button.pack()

    def next(self):
        self.place_forget()
        challenge_frame = ChallengeFrame(self.master, self.modules_frame, self.level, 0, 0, self.user)
        challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
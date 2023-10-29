import tkinter as tk
from challenge_frame import ChallengeFrame

class QuizFrame(tk.Frame):
    def __init__(self, master, modules_frame, level, question_index, user):
        super().__init__(master)
        self.modules_frame = modules_frame
        self.level = level
        self.question_index = question_index
        self.user = user
        self.quiz = level.quiz
        
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
            challenge_frame = ChallengeFrame(self.master, self.modules_frame, self.level, 0, self.user)
            challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def next_question(self):
        self.place_forget()
        next_question_frame = QuizFrame(self.master, self.modules_frame, self.level, self.question_index + 1, self.user)
        next_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def submit(self):
        answer = self.answer.get()

        if answer:
            if int(answer) == self.quiz_question['correct_answer']:
                # Update progress tracker. Score increment by 1
                self.next_question()
            else:
                # Update progress tracker ? Score doesn't go up
                self.next_question()
        else:
            level_name_message = tk.Label(self, text="Please select an answer.")
            level_name_message.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)


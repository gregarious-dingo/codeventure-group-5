import tkinter as tk

class ChallengeFrame(tk.Frame):
    def __init__(self, master, module_frame, level, challenge_index, challenge_score, user, learner_answers=[]):
        super().__init__(master)
        self.level = level
        self.challenge = level.challenge.challenges
        self.challenge_index = challenge_index
        self.challenge_score = challenge_score
        self.module_frame = module_frame
        self.user = user
        self.learner_answers = learner_answers

        if self.challenge == None:
            self.place_forget()
            self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        elif self.challenge_index != len(self.challenge):
            self.current_challenge = self.challenge[challenge_index]
            self.challenge_question = self.current_challenge['question']

            challenge_instruction = tk.Label(self,
                                             text='Please use double quotation ("), and leave a space after every variable assignment\n'+
                                             'For example: variable1 = "my string"')
            challenge_instruction.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)

            challenge_message = tk.Label(self, text=f"{self.challenge_question} \n\n\nEnter your answer:")
            challenge_message.grid(row=1, column=0, columnspan=2, padx=10, pady=20, sticky=tk.N)


            self.answer_text = tk.Text(self, height=8)
            self.answer_text.grid(row=3, column=1, sticky=tk.N)

            submit_button = tk.Button(self, text="Submit", command=self.submit)
            submit_button.grid(row=6, columnspan=2, pady=50)
        else:
            num_of_challenges = len(self.challenge)
            self.user.progress_tracker.update_challenge_score(self.level.level, self.challenge_score, num_of_challenges)
            challenge_result_frame = ChallengeResultFrame(self.master,
                                                          self.module_frame,
                                                          self.level,
                                                          self.learner_answers,
                                                          self.user)
            challenge_result_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def next_challenge(self):
        self.place_forget()
        next_challenge_frame = ChallengeFrame(self.master, 
                                              self.module_frame, 
                                              self.level, 
                                              self.challenge_index + 1, 
                                              self.challenge_score,
                                              self.user)
        next_challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def submit(self):
        answer=self.answer_text.get('1.0', 'end').strip()
        self.learner_answers.append(answer)
        print(type(self.learner_answers[0]))
        print(type(self.current_challenge['correct_answer']))

        if answer == self.current_challenge['correct_answer']:
            self.challenge_score += 1

            self.next_challenge()

        else:
            self.next_challenge()

class ChallengeResultFrame(tk.Frame):
    def __init__(self, master, module_frame, level, learner_answers, user):
        super().__init__(master)
        self.module_frame = module_frame
        self.level = level
        self.challenge = level.challenge.challenges
        self.learner_answers = learner_answers
        self.user = user

        challenge_result_message = tk.Label(self,
                                text="Your challenge results:",
                                font=("Arial Bold", 20))
        challenge_result_message.pack()

        challenge_num = 1
        answer_index = 0
        for challenge in self.challenge:
            correct_answer = challenge['correct_answer']
            if self.learner_answers[answer_index] == correct_answer:
                challenge = tk.Label(self,
                                    text=f"Challenge question {challenge_num}: {challenge['question']} ✔",
                                    bg='green')
                challenge.pack()

            else:
                challenge = tk.Label(self,
                                    text=f"Challenge question {challenge_num}: {challenge['question']} ✘",
                                    bg='red')
                challenge.pack()

            challenge_answer_comparison = tk.Label(self,
                                                   text=f"Your answer: {self.learner_answers[answer_index]}\n"
                                                   +f"{correct_answer}")
            challenge_answer_comparison.pack()
        
            challenge_num += 1
            answer_index += 1

        finish_button = tk.Button(self,
                                text='Finish',
                                command=self.finish)
        finish_button.pack()

    def finish(self):
        self.place_forget()
        self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
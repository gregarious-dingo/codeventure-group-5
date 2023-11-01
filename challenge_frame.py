import tkinter as tk

class ChallengeFrame(tk.Frame):
    def __init__(self, master, module_frame, level, challenge_index, challenge_score, user):
        super().__init__(master)
        self.level = level
        self.challenge = level.challenge.challenges
        self.challenge_index = challenge_index
        self.challenge_score = challenge_score
        self.module_frame = module_frame
        self.user = user

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
            self.place_forget()
            self.module_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
        if answer == self.current_challenge['correct_answer']:
            self.challenge_score += 1

            self.next_challenge()

        else:
            self.next_challenge()
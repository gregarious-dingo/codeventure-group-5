import tkinter as tk

class ChallengeFrame(tk.Frame):
    def __init__(self, master, module_frame, level, challenge_index, user):
        super().__init__(master)
        self.level = level
        self.challenge = level.challenge.challenges
        self.challenge_index = challenge_index
        self.module_frame = module_frame
        self.user = user

        if self.challenge_index != len(self.challenge):
            self.current_challenge = self.challenge[challenge_index]
            self.challenge_question = self.current_challenge['question']

            challenge_message = tk.Label(self, text=f"{self.challenge_question} \n\n\nEnter your answer:")
            challenge_message.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky=tk.N)

            self.answer = tk.StringVar()

            self.answer_entry = tk.Entry(self, textvariable=self.answer)
            self.answer_entry.grid(row=2, column=1, sticky=tk.W)

            register_button = tk.Button(self, text="Submit", command=self.submit)
            register_button.grid(row= 5, columnspan=2, pady=50)


    def next_challenge(self):
        self.place_forget()
        next_challenge_frame = ChallengeFrame(self.master, self.module_frame, self.level, self.challenge_index + 1, self.user)
        next_challenge_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def submit(self):
        answer=self.answer.get()

        if answer:
            if answer == self.current_challenge['correct_answer']:
                self.next_challenge()

            else:
                self.next_challenge()

        else:
            level_name_message = tk.Label(self, text="Please select an answer.")
            level_name_message.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)
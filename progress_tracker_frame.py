import tkinter as tk
from resources.progress_tracker import ProgressTracker
from collapsible_pane import cpane

class ProgressTrackerFrame(tk.Frame):
    def __init__(self, master, learner_frame, user):
        super().__init__(master)
        self.learner_frame = learner_frame

        selection_message = tk.Label(self, text=f'Doing great, {user.username}!')
        selection_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        row = 1
        for i in range(len(user.progress_tracker.quiz_scores)):
            level = user.progress_tracker.learning_modules.levels[i]
            level_name = level.name

            quiz_score_pane = cpane(self, f'{level_name} - Collapse', f'{level_name} - Expand')
            quiz_score_pane.grid(row=row, column=0, sticky=tk.N, pady=10)

            quiz_score = user.progress_tracker.quiz_scores[i]['score_display']
            if user.progress_tracker.challenge_scores[i] is not None:
                challenge_score = user.progress_tracker.challenge_scores[i]['score_display']
                display_score = tk.Label(quiz_score_pane.frame,
                        text=f'Quiz: {quiz_score}\nChallenge: {challenge_score}')
                display_score.grid(row=row+1, column=0, pady=10)

            else:
                display_score = tk.Label(quiz_score_pane.frame,
                                         text=f'Quiz: {quiz_score}')
                display_score.grid(row=row+1, column=0, pady=10)

            row+=1

        back_to_menu_button = tk.Button(self, text="Back to menu", command=self.back_to_menu)
        back_to_menu_button.grid(row=row+1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)


    def back_to_menu(self):
        self.place_forget()
        self.learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
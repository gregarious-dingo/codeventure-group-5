import tkinter as tk
from resources.progress_tracker import ProgressTracker
from collapsible_pane import cpane

class ProgressTrackerFrame(tk.Frame):
    def __init__(self, master, learner_frame, user, is_parent, is_educator, users=None):
        super().__init__(master)
        self.learner_frame = learner_frame

        title = tk.Label(master=self,
                                text="Progress Tracker",
                                font=("Arial Bold", 22))
        title.grid(row=0, columnspan=2, padx=10, pady=10)

        if is_parent or is_educator:
            welcome_message = tk.Label(self, text=f"{user.username}'s progress. Select a lesson to see the score:")
            welcome_message.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)
        else:
            welcome_message = tk.Label(self, text=f'Doing great, {user.username}! Select a lesson to see your scores:')
            welcome_message.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        row = 2
        for i in range(0, len(user.progress_tracker.quiz_scores), 2):
            levels = user.progress_tracker.learning_modules.levels
            level_left = levels[i]
            level_right = levels[i + 1] if i + 1 < len(levels) else None
            
            left_frame = tk.Frame(self)
            right_frame = tk.Frame(self)

            left_frame.grid(row=row, column=0, padx=35, pady=10, sticky=tk.E)
            right_frame.grid(row=row, column=1, padx=0, pady=10, sticky=tk.W)

            quiz_score_left_pane = cpane(left_frame, f'{level_left.name} - Collapse', f'{level_left.name} - Expand')
            quiz_score_left_pane.grid(row=row, column=0, padx=5, pady=5, sticky=tk.E)

            quiz_score_right_pane = cpane(right_frame, f'{level_right.name} - Collapse', f'{level_right.name} - Expand')
            quiz_score_right_pane.grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)

        
            for j in range(2):
                quiz_score = user.progress_tracker.quiz_scores[i + j]['score_display']
                challenge_score = user.progress_tracker.challenge_scores[i + j]['score_display'] \
                    if user.progress_tracker.challenge_scores[i + j] is not None else None

                display_score = tk.Label(
                    quiz_score_left_pane.frame if j == 0 else quiz_score_right_pane.frame,
                    text=f'Quiz: {quiz_score}\nChallenge: {challenge_score}' if challenge_score is not None else f'Quiz: {quiz_score}'
                )
                display_score.grid(row=0, column=0, pady=10)

            row+=1

        back_to_menu_button = tk.Button(self, text="Back to menu", command=self.back_to_menu)
        back_to_menu_button.grid(row=row+1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)


    def back_to_menu(self):
        self.place_forget()
        self.learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
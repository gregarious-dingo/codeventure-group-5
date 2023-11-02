import tkinter as tk
from progress_tracker_frame import ProgressTrackerFrame

class EducatorFrame(tk.Frame):
    """
    Menu frame for when user logins as Educator.
    Feature of Educator:
    Check any Learners' progress
    """
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.login_frame = login_frame
        self.user = user

        welcome_message = tk.Label(self, text=f'Welcome {user.username}')
        welcome_message.grid(row=1, columnspan=2, sticky=tk.NW, padx=10, pady=10)

        check_progress_button = tk.Button(self, text="Check learners' progress",
                                          command = self.check_progress)
        check_progress_button.grid(row=3, column=0, sticky=tk.N)

        back_to_login_button = tk.Button(self, text="Log Out", command=self.log_out)
        back_to_login_button.grid(row=10, columnspan=2)

    def check_progress(self):
        self.place_forget()
        selection_frame = EducatorSelectLearnerFrame(self.master, self, self.user)
        selection_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def log_out(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

class EducatorSelectLearnerFrame(tk.Frame):
    """
    Display a listbox that shows a list of Learners for the educator to choose from.
    When one of the learners is clicked, their progress tracker is shown.
    """
    def __init__(self, master, educator_frame, user):
        super().__init__(master)
        self.educator_frame = educator_frame
        self.user = user

        prompt_question = tk.Label(self, text="Which learner's progress do you want to check?")
        prompt_question.pack(side=tk.TOP)

        list_items = tk.Variable(value=user.learners)

        learner_list = tk.Listbox(self,
                                  listvariable=list_items,
                                  height=len(self.user.learners),
                                  selectmode=tk.SINGLE)
        
        learner_list.pack(fill=tk.BOTH)

        back_button = tk.Button(self,
                                text="Back to menu",
                                command=self.back_to_educator_menu)
        back_button.pack()



        def check_selected_learner(event):
            self.place_forget()
            selected_learner = learner_list.curselection()
            learner = [learner_list.get(i) for i in selected_learner]
            for account in self.user.learners:
                if account.username == learner[0]:
                    sel_learner = account
            learner_progress_frame = ProgressTrackerFrame(self.master,
                                                          self,
                                                          sel_learner,
                                                          False,
                                                          True)
            learner_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        learner_list.bind('<<ListboxSelect>>', check_selected_learner)

    def back_to_educator_menu(self):
        self.place_forget()
        self.educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
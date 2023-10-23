from users.user import User

class Parent(User):
    def __init__(self, username, password, learner):
        super().__init__(username, password)
        self.account_type = "Parent"
        self.learner = learner

    def block_learner(self):
        self.learner.blocked = True
        
    def unblock_learner(self):
        self.learner.blocked = False

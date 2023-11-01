from users.user import User
from resources.progress_tracker import ProgressTracker

class Learner(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.account_type = "Learner"
        self.progress_tracker = ProgressTracker()
        self.blocked = False

    def __str__(self) -> str:
        return self.username

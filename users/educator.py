from users.user import User
from resources.progress_tracker import ProgressTracker

class Educator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.progress_tracker = ProgressTracker()
        self.account_type = "Educator"
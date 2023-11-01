# CodeVenture - FRI 1000 Group 5

## Overview

CodeVenture is a learning management application built with Python and tkinter. It provides a user-friendly interface for learners, parents, and educators to access learning modules, take quizzes and challenges, track progress, and manage user accounts.

## Features

- User Registration and Login
  - Users can create a new account by providing a username, password, and selecting their user type (Learner, Educator, or Parent).
  - Registered users can log in with their credentials.

- User Types
  - Learners: Access learning modules, take quizzes and challenges, and track progress.
  - Educators: (Not Yet)
  - Parents: Check their child's progress, toggle account access, and log out.

- Learner Features
  - Select Learning Modules: Choose from a list of available learning modules.
  - Progress Tracking: Track quiz and challenge scores for different learning levels.
  - Quizzes: Take quizzes related to learning modules.
  - Challenges: Complete open-ended challenges.

## How to Run

1. **Prerequisites:**
   - Python 3.x installed on your system.
   - Required libraries (tkinter).

2. **Navigate to the project directory:**
   - Open your terminal/command prompt and use the `cd` command to navigate to your project directory:

   ```shell
   cd codeventure-group-5
   ```

3. **Run the application**
   ```shell
   python interface.py
   ```

4. **Features**
  - Register: Allows the user to register an account of three types (Learner, Parent, Educator)
  - Login: Allows the user to login to an existing account
  - Logout: Allows the user to logout of their account
  
  # Learner
  - Learning Module: Allows the user to learn about Python concepts, attempt quizzes and challenges
  - Progress Tracker: Allows the user to 

  # Parent
  - Register: When registering, the user will be prompt to name their child
  - Progress Tracker: Allows the user to check the progress of their child
  - Block Account: Allows the user to block their child's progress

  # Educator
  - Progress Tracker: Allows the user to check the progress of all learners (Not yet implemented)
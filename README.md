# CodeVenture - FRI 1000 Group 5

## Overview

CodeVenture is a learning management application built with Python and tkinter. It provides a user-friendly interface for learners, parents, and educators to access learning modules, take quizzes and challenges, track progress, and manage user accounts.

This project is designed to meet the core requirements of FIT1055, ensuring reliability by its simplicity. It may not encompass a range of features but it is aligned our goals to build a solid foundation that aligns with the learning outcomes as well as act as a stable platform for potential future expansion.

## Features

- User Registration and Login
  - Users can create a new account by providing a username, password, and selecting their user type (Learner, Educator, or Parent).
  - Registered users can log in with their credentials.

- User Types
  - Learners: Access learning modules, take quizzes and challenges, track progress, and log out.
  - Educators: Check all learners' progress, and log out
  - Parents: Check their child's progress, toggle account access, and log out.

- Learner Features
  - Select Learning Modules: Choose from a list of available learning modules.
  - Progress Tracking: Track quiz and challenge scores for different learning levels.
  - Quizzes: Take quizzes related to learning modules.
  - Challenges: Complete open-ended challenges.

- Parent Features
  - Progress Tracker: Allows the user to check the progress of their child.
  - Block Account: Allows the user to block their child's progress.

- Educator Features
  - Progress Tracker: Allows the user to check the progress of all learners.

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

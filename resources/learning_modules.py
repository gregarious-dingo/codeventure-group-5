from utils.utils import Utils
from resources.quiz import Quiz
from resources.challenge import Challenge

class Learning_Modules:
    def __init__(self):
        self.levels = lessons
    
    def add_level(self, level):
        self.levels.append(level)
    
    def select_level(self, learner):
        print("Available Levels:")
        for i, level in enumerate(self.levels):
            print(f"{i + 1}. {level.name}")
        
        selected_lvl = input("Select a level by entering the number (Enter 0 to quit):\n")

        try:
            selected_lvl = int(selected_lvl)
            if 1 <= selected_lvl <= len(self.levels):
                self.study_level(self.levels[selected_lvl - 1], learner)
            elif selected_lvl == 0:
                return
            else:
                Utils.display_str("Please enter a valid level.")
        
        except ValueError:
            print("Please enter a valid level number.")

    def study_level(self, level, learner):
        print(f"You have selected the {level.name} level.")
        print("Study notes:\n")
        level.print_learning_materials()

        input("\nReady to enter the quiz? Press Enter to start!")
        level.quiz.start(level, learner)

        if level.challenge:
            input("\nReady to enter the challenge? Press Enter to start!")
            level.challenge.start(level, learner)

class Level:
    def __init__(self, level, name, learning_materials, quiz, challenge=None):
        self.level = level
        self.name = name
        self.learning_materials = learning_materials
        self.quiz = quiz
        self.challenge = challenge

    def print_learning_materials(self):
        for material in self.learning_materials:
            print(material)

'''
    an example usage of the code is as below:
    Level("LEVEL NAME",
         ["LESSON HEADING",
         "LESSON CONTENT"
         "ANOTHER LINE OF LESSON CONTENT"],
         
         [
         {"question": "QUESTION",
         "options": ["OPTION 1", "OPTION 2", "OPTION 3"]
         "correct_answer:" OPTION},
         
        {"question": "QUESTION",
        "options": ["OPTION 1", "OPTION 2", "OPTION 3"]
        "correct_answer:" OPTION},
        ])
'''

lessons = [
    Level(1, "Lesson 1: What is Python?",
        ["Welcome to Python! Python is a text-based programming language used to tell a computer what to do",
        "For example, if you have a robot friend, you want to teach it to do things.",
        "You would do so by using Python and not the English language. This will give",
        "the computer a set of simple and clear instructions. By communicating in this way",
        "your robot friend will be able to do all sorts of cool things like playing games!\n\n"
                  
        'For example, to teach a computer to say "Hello, world!", we type print("Hello, world")',
        'The "print" is commanding the computer to speak, while "Hello, world!" is what it will speak'],
        Quiz([{"question": "What is Python?", 
            "options": ["A text-based programming language", "A human language", "A dog's name"],
            "correct_answer": 1},
            {"question": "What does print do?",
            "options": ["Asks the robot to play a game", "Commanding a computer to speak", "Printing on a paper"], 
            "correct_answer": 2}]),
        Challenge([
            {
                "question": 'Enter code that prints this string: "Hello Coders!"',
                "correct_answer": 'print("Hello Coders!")'
            },
        ]
            )),

    Level(2, "Lesson 2: Variables in Python",
        ["In Python, a variable is like a container that can hold different types of information.",
        "You can think of it as a box that stores data. These boxes have labels called variable names.",
        "For example, if you want to store the number 42 in a variable, you can do it like this:",
        "my_variable = 42",
        "Now, `my_variable` holds the value 42, and you can use it in your programs."],
        Quiz([{"question": "What is a variable in Python?",
            "options": ["A box that can hold data", "A type of snake", "A type of function"],
            "correct_answer": 1},
            {"question": "How do you assign a value to a variable?",
            "options": ["Using the `=` operator", "Using the `+` operator", "Using the `if` statement"],
            "correct_answer": 1}]),
        Challenge([
            {
                "question": 'Define a variable `my_name` and assign "Evan" to it.',
                "correct_answer": 'my_name = "Evan"'
            },
            {
                "question": 'Print out the variable you just created!',
                'correct_answer': 'print(my_name)'
            }
        ])),

    Level(3, "Lesson 3: Control Flow",
        ["Introduction to if statements",
         'An "if statement" is a fundamental control structure in Python and many other programming languages.',
         'It allows you to make decisions in your code based on certain conditions. In simple terms, you can think',
         'of an if statement as a way to tell the computer, "If a particular condition is met, do one thing; otherwise, do something else.',
         'An if statement is in this form:', 
         'if (boolean statement):',
         '    do something',
         "Introduction to loops",
         'A "for loop" in Python is used for iterating over a sequence (such as a list, tuple, string, or range) and performing a set of actions for each item in the sequence. ',
         "It allows you to automate repetitive tasks by executing the same code multiple times with different data." ],
        Quiz([{"question": "What is an if statement used for?",
            "options": ["Iterating over a sequence of items", "Making decisions in code", "Defining a function"],
            "correct_answer": 2},
            {"question": "What type of loop can be used to iterate over a list?",
            "options": ["for loop", "while loop", "if-else loop"],
            "correct_answer": 1}]),
        Challenge([
            {
                "question": "Write an if statement to check if a variable (num) is even. Write code up until the colon, including it. ",
                "correct_answer": 'if num % 2 == 0:'
            },
        ])),

    Level(4, "Lesson 4: Lists and Arrays",
        ["Lists and arrays are used to store collections of items in Python.",
        "They are ordered and can hold different types of data, including numbers, strings, and more.",
        "You can access and manipulate the elements of a list using indexes.",
        "Let's dive into the world of lists and arrays."],
        Quiz([{"question": "What is a list in Python?",
            "options": ["A way to store a single value", "A collection of items", "A mathematical operation"],
            "correct_answer": 2},
            {"question": "How do you access an element in a list?",
            "options": ["Using parentheses", "Using curly braces", "Using square brackets"],
            "correct_answer": 3}]),
        Challenge([
            {
                "question": "create a list called my_list which has the values 1, 2 and 3 inside.",
                "correct_answer": 'my_list = [1, 2, 3]'
            },
            {
                "question": "Challenge 2: Access and print the second element of my_list.",
                "correct_answer": 'print(my_list[1])'
            }])),

    Level(5, "Lesson 5: Functions",
        ["Functions are blocks of code that can be called with specific inputs,",
        "and they perform a specific task or calculation. Functions are reusable pieces of code.",
        "We can define our own functions in Python. Let's explore how to do that."],
        Quiz([{"question": "What is a function in Python?",
            "options": ["A variable", "A block of code that performs a specific task", "A data structure"],
            "correct_answer": 2},
            {"question": "How do you define a function in Python?",
            "options": ["Using square brackets", "Using the 'func' keyword", "Using the 'def' keyword"],
            "correct_answer": 3}]),
        Challenge([
            {
                "question": "Declare a function called add_numbers which takes in two arguments, num1 and num2. Write code until the colon., including it ",
                "correct_answer": 'def add_numbers(num1, num2):'
            },
            {
                "question": "Implement the function you just declared, adding the two numbers and returning it. Write code in one line.",
                "correct_answer": 'return num1 + num2'
            }])),

    Level(6, "Lesson 6: Dictionaries",
        ["Dictionaries in Python are collections of key-value pairs.",
        "Each key is unique and maps to a specific value. Dictionaries are unordered.",
        "They are useful for storing data that needs to be quickly looked up by a unique key.",
        "Let's explore how dictionaries work."],
        Quiz([{"question": "What is a dictionary in Python?",
            "options": ["A collection of key-value pairs", "A type of loop", "A mathematical concept"],
            "correct_answer": 1},
            {"question": "How do you access a value in a dictionary?",
            "options": ["Using square brackets with the key", "Using parentheses", "Using quotation marks"],
            "correct_answer": 1}]),
        Challenge([
            {
                "question": "Create an empty dictionary called my_dict.",
                "correct_answer": 'my_dict = {}'
            },
            {
                "question": 'Add a key-value pair to my_dict where the key is "name" and the value is the string "Evan".',
                "correct_answer": 'my_dict["name"] = "Evan"'
            }])),

    Level(7, "Lesson 7: Modules and Libraries",
        ["Python provides a rich ecosystem of modules and libraries that extend its capabilities.",
        "Modules are collections of Python code that can be used in your programs.",
        "In this lesson, we will learn how to import and use modules and libraries."],
        Quiz([{"question": "What are modules in Python?",
            "options": ["A type of variable", "Collections of Python code", "Functions with no arguments"],
            "correct_answer": 2},
            {"question": "How do you import a module in Python?",
            "options": ["Using the 'import' statement", "Using parentheses", "Using single quotes"],
            "correct_answer": 1}]),
        Challenge([
            {
                "question": "Import a library called tkinter and save it as tk.",
                "correct_answer": 'import tkinter as tk'
            }
            ])),

    Level(8, "Lesson 8: Strings and Text Manipulation",
        ["In Python, strings are used to represent text. You can perform various operations",
        "on strings, such as concatenation, slicing, and formatting.",
        "Let's explore how to work with strings and manipulate text."],
        Quiz([
            {"question": "What is a string in Python?",
            "options": ["A collection of numbers", "A sequence of text characters", "A mathematical operation"],
            "correct_answer": 2},
            {"question": "How do you concatenate two strings in Python?",
            "options": ["Using the '+' operator", "Using the 'add' function", "Using the 'concat' method"],
            "correct_answer": 1}]),
        Challenge([
            {
                "question": "Create a string variable called 'my_string' with the value 'Hello, World!'.",
                "correct_answer": 'my_string = "Hello, World!"'
            },
            {
                "question": "Concatenate 'my_string' with ' Python' and store the result in a new variable called 'result_string'.",
                "correct_answer": 'result_string = my_string + " Python"'
            }])),

    Level(9, "Lesson 9: Conditional Statements",
        ["Conditional statements allow you to make decisions in your code.",
        "You can use 'if', 'elif', and 'else' to control the flow of your program based on conditions.",
        "Let's dive into conditional statements and how to use them effectively."],
        Quiz([{"question": "What is the purpose of 'if' statements in Python?",
            "options": ["To repeat a block of code", "To make decisions based on conditions", "To define functions"],
            "correct_answer": 2},
            {"question": "What does 'elif' stand for in Python?",
            "options": ["Element List If", "Else If", "End Loop If"],
            "correct_answer": 2}]),
        Challenge([
            {
                'question': 'Enter an if statement that checks whether an integer, num is a factor of 15. Write code until the colon, including it. ',
                'correct_answer': 'if num % 15 == 0:'
            },
            {
                'question': "Let's say the first if statement fails. Enter another statement that checks if num is even, write until the colon.",
                'correct_answer': 'elif num % 2 == 0:'
            }
        ])),

    Level(10, "Lesson 10: Error Handling",
         ["Error handling in Python allows you to handle unexpected situations gracefully.",
          "You can use 'try', 'except', 'finally', and 'raise' to manage errors in your code.",
          "Let's explore how to handle errors effectively."],
         Quiz([{"question": "What is the purpose of 'try' and 'except' blocks in Python?",
           "options": ["To define functions", "To handle errors gracefully", "To create loops"],
           "correct_answer": 2},
          {"question": "What is the purpose of 'finally' block in Python?",
           "options": ["To raise an error", "To define functions", "To specify the final answer"],
           "correct_answer": 3}])),
]


if __name__ == "__main__":
    lm = Learning_Modules()
    lm.select_level()

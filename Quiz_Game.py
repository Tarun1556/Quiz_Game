quiz_questions = [

    {
        "question": "Which language is known as the language of the web?",
        "options": ["A. Python", "B. C++", "C. JavaScript", "D. Java"],
        "answer": "C"
    },

    {
        "question": "Which data structure uses a LIFO (Last In, First Out) method?",
        "options": ["A. Queue", "B. Stack", "C. Linked List", "D. Array"],
        "answer": "B"
    },
    {
        "question": "Which data structure is used to implement recursion?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "A"
    },
    {
        "question": "In a linked list, each node contains a data part and a ______ part.",
        "options": ["A. Link", "B. Pointer", "C. Value", "D. Index"],
        "answer": "B"
    },
    {
        "question": "Which data structure is the best choice for implementing a priority queue?",
        "options": ["A. Array", "B. Stack", "C. Heap", "D. Linked List"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a linear data structure?",
        "options": ["A. Graph", "B. Tree", "C. Queue", "D. Heap"],
        "answer": "C"
    },
    {
        "question": "What is the time complexity of searching an element in a binary search tree (BST) in the best case?",
        "options": ["A. O(n)", "B. O(log n)", "C. O(n^2)", "D. O(1)"],
        "answer": "B"
    },
    {
        "question": "Which data structure is used in Breadth-First Search (BFS) of a graph?",
        "options": ["A. Stack", "B. Queue", "C. Linked List", "D. Tree"],
        "answer": "B"
    }
]





def ask_question(question_data):
    """Ask a single question, get user input, validate, and return if it was correct."""
    print(f"Question: {question_data['question']}")
    for option in question_data['options']:
        print(option)

    # Input validation loop
    while True:
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    # Check if the answer is correct and give feedback
    if user_answer == question_data['answer']:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong. The correct answer was {question_data['answer']}.\n")
        return False


def quiz_game(questions):
    """Run the quiz game and track the user's score."""
    score = 0
    print("Welcome to the Quiz Game!\n")

    # Loop through questions and ask each one
    for question_data in questions:
        if ask_question(question_data):
            score += 1

    # Display the final score
    print(f"Your final score is {score} out of {len(questions)}.")


# Start the quiz game
quiz_game(quiz_questions)

'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/20
Description: [Lab 4 project description]
'''

import random

def read_file_to_dict():
    """
    1. This function reads the contents of a file (in this case, StateCapitals.txt) and
    converts it into a dictionary.
    2. Each line in the file is expected to be in the format State,Capital.
    3. The function strips any extra whitespace, splits the line into state and capital,
    and stores them in a dictionary where the state is the key and the capital is the value.
    """
    pass

def get_random_state():
    """
    1. This function takes the dictionary of states and capitals as input.
    2. It randomly selects a state and its corresponding capital from the dictionary and
    returns them as a tuple.
    """
    pass

def get_random_choices():
    """
    1. This function generates a list of four possible answers for a quiz question.
    2. It starts with the correct capital and then randomly selects three other capitals
    from the list of all capitals, ensuring they are not the same as the correct capital or each other.
    3. Finally, it shuffles the list to randomize the order of the answers.
    """
    pass

def ask_question():
    """
    1. This function displays the quiz question to the user, showing the state and the four
    possible capitals.
    2. It prompts the user to enter their selection (A, B, C, or D) and validates the input.
    3. If the input is valid, it converts the selection to a corresponding index
    (0 for A, 1 for B, etc.) and returns it.
    """
    pass

def main():
    """
    1. This is the main function that runs the quiz.
    2. It reads the state capitals from the file into a dictionary.
    3. It initializes a score counter (points) to 0.
    4. It runs a loop for 10 questions:
    5. Randomly selects a state and its capital.
    6. Generates four possible answers (one correct and three incorrect).
    7. Prompts the user to answer the question.
    8. Checks if the user's answer is correct and updates the score accordingly.
    9. Finally, it prints the user's score at the end of the quiz.
    """
    pass

if __name__ == "__main__":
    main()

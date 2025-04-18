'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/02/20
Description: This project allows users to test their knowledge on US states and capitals! Over the course of 10 questions,
the user will be prompted to answer from a multiple choice selection choices A-D, with a state given in the question, to
respond with the corresponding capital. At the end of the 10 questions, they get a final score.
'''

import random

def read_file_to_dict(file_name: str) -> dict:
    """
    1. This function reads the contents of a file (in this case, StateCapitals.txt) and
    converts it into a dictionary.
    2. Each line in the file is expected to be in the format State,Capital.
    3. The function strips any extra whitespace, splits the line into state and capital,
    and stores them in a dictionary where the state is the key and the capital is the value.

    Args:
        file_name (str): the path to the file name, expressed as a string
    Returns:
        The dictionary containing all the states and capitals in the form of a (key, value) pair
    """
    file = open(file_name).readlines()
    capital_list = list()
    capital_dictionary = dict()

    for line in file:
        item = line.strip("\n").split(",")
        capital_list.append(item)
    
    for row in capital_list:
        capital_dictionary[row[0]] = row[1]
    
    return capital_dictionary

def get_random_state(states: dict) -> tuple:
    """
    1. This function takes the dictionary of states and capitals as input.
    2. It randomly selects a state and its corresponding capital from the dictionary and
    returns them as a tuple.

    Args:
        states (dict): the dictionary of states and capitals
    Returns:
        A tuple of a random (state, capital) pairing
    """
    pairing = random.choice(list(states.items()))
    return pairing

def get_random_choices(states: dict, correct_capital: str) -> list:
    """
    1. This function generates a list of four possible answers for a quiz question.
    2. It starts with the correct capital and then randomly selects three other capitals
    from the list of all capitals, ensuring they are not the same as the correct capital or each other.
    3. Finally, it shuffles the list to randomize the order of the answers.

    Args:
        states (dict): the dictionary of states and capitals
        correct_capital (str): the correct capital choice which will be appended to a list of 4 choices
    Returns:
        A list of 4 capital choices: 1 correct, 3 incorrect
    """
    possible_answers = list()
    all_capitals = list(states.values())
    random.shuffle(all_capitals)

    for i in range(3):
        possible_answers.append(all_capitals[i])

    possible_answers.append(correct_capital)
    random.shuffle(possible_answers)

    return possible_answers

def ask_question(correct_state: str, possible_answers: list) -> int:
    """
    1. This function displays the quiz question to the user, showing the state and the four
    possible capitals.
    2. It prompts the user to enter their selection (A, B, C, or D) and validates the input.
    3. If the input is valid, it converts the selection to a corresponding index
    (0 for A, 1 for B, etc.) and returns it.

    Args:
        correct_state (str): the correct state by which the user will attempt to find its matching capital
        possible_answers (list): the list of 4 possible capital choices, of which 1 is correct, and 3 incorrect
    Returns:
        An integer value corresponding to the user's choice (0 - A, 1 - B, 2 - C, 3 - D)
    """
    answer_index = 0
    valid = False

    print(f"The capital of {correct_state} is:")
    print(f"    A. {possible_answers[0]}    B. {possible_answers[1]}    C. {possible_answers[2]}    D. {possible_answers[3]}")
    
    while not valid:
        try:
            user_input = input("Enter selection: ").upper()
            if user_input in ('A', 'B', 'C', 'D'):
                valid = True
            else:
                print("Invalid input. Input choice A-D.")
        except ValueError:
            print("Invalid input. Input choice A-D.")
    
    match user_input:
        case 'A':
            answer_index = 0
        case 'B':
            answer_index = 1
        case 'C':
            answer_index = 2
        case 'D':
            answer_index = 3
    
    return answer_index

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
    # read the contents of the statecapitals.txt file
    states_and_capitals = read_file_to_dict("Lab 4\\statecapitals.txt")

    print("- State Capitals Quiz -")

    # initialize question number and score 
    questions = 1
    points = 0

    while questions <= 10:

        # get a random tuple of (state, capital)
        random_pair = get_random_state(states_and_capitals)

        # get 4 possible capital answers: 1 correct, 3 incorrect, list shuffled
        random_capitals = get_random_choices(states_and_capitals, random_pair[1])

        # ask user question and update scores accordingly
        print(f'{questions}.', end = ' ')
        user_choice = ask_question(random_pair[0], random_capitals)
        if random_capitals[user_choice] == (random_pair[1]):
            print("Correct!")
            points += 1
        else:
            print(f"Incorrect. The correct answer is {random_pair[1]}")

        questions += 1

    print(f"End of test. You got {points} correct.")


if __name__ == "__main__":
    main()

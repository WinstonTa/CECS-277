'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/05/01
Description: This project lets users interface a task list and essentially use a basic to-do app. The user can view
current tasks, mark tasks as complete, search by date, and assign new tasks to their list of to-do items.
'''

# file imports
import check_input

def main_menu() -> int:
    """
    Displays the main menu and returns the user’s valid input.

    Returns:
        An integer representing the user's valid input.
    """
    tasks_left = 7
    print(f"Tasks to complete: {tasks_left}")
    user_choice = check_input.get_int_range("1. Display current task\n2. Display all tasks\n3. Mark current task complete\
                                            \n4. Add new tasks\n5. Search by date\n6. Save and quit\nEnter choice: ", 1, 6)
    
    return user_choice

def get_date() -> str:
    """
    Prompts the user to enter the month, day, and year. Valid months are 1-12, valid days are 1-31,
    and valid years are 2000-2100 (no need to verify that it is a correct day for the month
    (ie. Feb 31 st is valid)). Return the date in the format:MM/DD/YYYY. If the inputted month or day
    is less than 10, then add a 0 to format it correctly."""
    user_month = "{:02d}".format(check_input.get_int_range("Enter month: ", 1, 12))
    user_day = "{:02d}".format(check_input.get_int_range("Enter day: ", 1, 31))
    user_year = "{:04d}".format(check_input.get_int_range("Enter year: ", 2000, 2100))

    print(f"{user_month}/{user_day}/{user_year}")

def get_time():
    """
    Prompts the user to enter the hour (military time) and minute. Valid hours are 0-23 and valid
    minutes are 0-59. Return the date in the format: HH:MM. If the inputted hour or minute is less than
    10, then add a 0 to format it correctly.
    """
    pass

def main():
    print("-Tasklist-")
    get_date()
    main_menu()

if __name__ == "__main__":
    main()

'''
Name(s): Winston Ta, Mindy Yun
Date: 2025/05/01
Description: This project lets users interface a task list and essentially use a basic to-do app. The user can view
current tasks, mark tasks as complete, search by date, and assign new tasks to their list of to-do items.
'''

# file imports
import check_input
import tasklist

def main_menu():
    """
    Displays the main menu and returns the user’s valid input.

    Returns:
        An integer representing the user's valid input.
    """
    user_tasks = tasklist.TaskList()
    
    while True:
        print("-Tasklist-")
        print(f"Tasks to complete: {len(user_tasks)}")
        user_choice = check_input.get_int_range("1. Display current task\n2. Display all tasks\n3. Mark current task complete\
                                                \n4. Add new tasks\n5. Search by date\n6. Save and quit\nEnter choice: ", 1, 6)
        
        if user_choice == 1:
            print(f"Current task is:\n{user_tasks.get_current_task()}")
        elif user_choice == 2:
            if len(user_tasks) == 0:
                print("There are no tasks.")
            else:
                for i, task in enumerate(user_tasks._tasklist, start = 1):
                    print(f"{i}. {task}")
        elif user_choice == 3:
            print(f"Marking Current task as complete:\n{user_tasks.get_current_task()}")
            user_tasks.mark_complete()
        elif user_choice == 4:
            task_name = input("Enter a task: ")
            user_date = get_date()
            user_time = get_time()
            user_tasks.add_task(task_name, user_date, user_time)
        elif user_choice == 5:
            print("Enter date to search: ")
            search_date = get_date()

            for i, task in enumerate(user_tasks._tasklist, start = 1):
                if task._date == search_date:
                    print(f"{i}.{task}")
        else:
            print("Saving list...")
            user_tasks.save_file()
            break
    
def get_date() -> str:
    """
    Prompts the user to enter the month, day, and year. Valid months are 1-12, valid days are 1-31,
    and valid years are 2000-2100 (no need to verify that it is a correct day for the month
    (ie. Feb 31 st is valid)). Return the date in the format:MM/DD/YYYY. If the inputted month or day
    is less than 10, then add a 0 to format it correctly.

    Returns:
        A string in format MM/DD/YYYY representing the date that a user inputted.
    """
    user_month = "{:02d}".format(check_input.get_int_range("Enter month: ", 1, 12))
    user_day = "{:02d}".format(check_input.get_int_range("Enter day: ", 1, 31))
    user_year = "{:04d}".format(check_input.get_int_range("Enter year: ", 2000, 2100))

    return f"{user_month}/{user_day}/{user_year}"

def get_time() -> str:
    """
    Prompts the user to enter the hour (military time) and minute. Valid hours are 0-23 and valid
    minutes are 0-59. Return the date in the format: HH:MM. If the inputted hour or minute is less than
    10, then add a 0 to format it correctly.

    Returns:
        A string in format HH:MM representing the time that a user inputted.
    """
    user_hour = "{:02d}".format(check_input.get_int_range("Enter hour: ", 0, 23))
    user_minute = "{:02d}".format(check_input.get_int_range("Enter minute: ", 0, 59))

    return f"{user_hour}:{user_minute}"

if __name__ == "__main__":
    main_menu()

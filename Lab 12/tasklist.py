import task

class TaskList():
    def __init__(self):
        # initialize task list
        self._tasklist = []

        # open task list file
        task_file = open("Lab 12\\tasklist.txt")
        task_file.readlines()

        # file opening
        with open("Lab 12\\tasklist.txt") as file:
            contents = file.readlines()
            for line in contents:
                desc, date, time = line.split(",")
                task_item = task.Task(desc, date, time)
                self._tasklist.append(task_item)
        
        self._tasklist.sort()

    def add_task(self, desc: str, date: str, time: str):
        """
        Allows users to add tasks to the task list.

        Args:
            desc (str): The name of the task.
            date (str): The date of the task.
            time (str): The time of the task.
        """
        new_task = task.Task(desc, date, time)
        self._tasklist.append(new_task)
        self._tasklist.sort()

    def get_current_task(self):
        """
        Returns the current task at the top of the list.

        Returns:
            A string describing the current task.
        """
        return self._tasklist[0]

    def mark_complete(self) -> task:
        """
        Marks current task as complete.

        Returns:
            The task at the top of the list, done through pop() method.
        """
        return self._tasklist.pop()

    def save_file(self):
        """
        Saves all tasks in the task file.
        """
        with open("tasklist.txt", "w") as file:
            for item in self._tasklist:
                file.write(f"{repr(item)}\n")
    
    def __len__(self):
        """return the number of items in the tasklist"""
        return len(self._tasklist)

    def __iter__(self):
        """initialize the iterator attribute n and return self."""
        self._n = 0
        return self

    def __next__(self):
        self._n += 1
        if self._n > self.__len__(self): raise StopIteration
        else: return self._tasklist[self._n - 1]



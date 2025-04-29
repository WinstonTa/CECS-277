import task

class TaskList():
    def __init__(self):
        self._tasklist = []

        task_file = open("Lab 12\\tasklist.txt")
        task_file.readlines()
        for i in range(len(task_file)):     # is this cheating
            print(task_file[i])

    def add_task(self, desc, date, time):
        new_task = task.Task(desc, date, time)
        self._tasklist.append(new_task)
        self._tasklist.sort()       # sus sorting, check later

    def get_current_task(self):
        return self._tasklist[0]

    def mark_complete(self):
        return self._tasklist.pop()

    def save_file(self):
        pass
    
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



task_file = open("Lab 12\\tasklist.txt")
task_list = task_file.readlines()

new_list = []
count = 0
for item in task_list:
    # strip it the \n part
    item = item.strip("\n")  

    # split by commas
    task_split = item.split(",")
    
    # create task object
    task_object = task.Task(task_split[0], task_split[1], task_split[2])
    if task_object < new_list[count] and count > 1:
        new_list.inert(count)
    else:
        new_list.append(task_object)
    count += 1

print(new_list)



class Task():
    def __init__(self, desc, date, time):
        self._desc = desc
        self._date = date
        self._time = time

    def __str__(self):
        return f"{self._desc} - Due: {self._date} at {self._time}"
    
    def __repr__(self): # come back to this part
        pass
    
    def __lt__(self, other):    # come back to this part 
        pass
        

class Task():
    def __init__(self, desc, date, time):
        self._desc = desc
        self._date = date
        self._time = time

    def __str__(self):
        return f"{self._desc} - Due: {self._date} at {self._time}"
    
    def __repr__(self): #come back to this
        pass
    def __lt__(self, other):
        # compare by year
        if int(self._date[-4:]) < int(other._date[-4:]): return True
        # compare by month
        if int(self._date[:2]) < int(other._date[:2]): return True
        # compare by day
        if int(self._date[3:5]) < int(other._date[3:5]): return True
        # compare by hour
        if int(self._time[:2]) < int(other._time[:2]): return True
        # compare by minute
        if int(self._time[-2:]) < int(other._time[-2:]): return True
        # compare by alphabetical order
        if self._desc < other._desc: return True
        return False
        
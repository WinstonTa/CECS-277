import abc

class Puppy_State(abc.ABC):
    @abc.abstractmethod
    def feed(self, puppy):
        # abstract feed method
        pass

    @abc.abstractmethod
    def play(self, puppy):
        # abstract play method
        pass

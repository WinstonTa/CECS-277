import abc

class Puppy_State(abc.ABC):
    @abc.abstractmethod
    def feed(self, puppy):
        pass

    @abc.abstractmethod
    def play(self, puppy):
        pass

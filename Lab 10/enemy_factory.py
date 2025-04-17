import abc

class EnemyFactory(abc.ABC):
    """creates a random enemy"""
    @abc.abstractmethod
    def create_random_enemy(self):
        pass

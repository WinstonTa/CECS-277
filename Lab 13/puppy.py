import state_asleep

class Puppy():
    def __init__(self):
        # initialize puppy
        self._state = state_asleep.State_Asleep()
        self._feeds = 0
        self._plays = 0

    def change_state(self, new_state):
        """
        Puppy changes state between being asleep, eating, or playing.

        Args:
            new_state (state): The desired new state of the puppy.
        """
        self._state = new_state

    def throw_ball(self) -> str:
        """
        Puppy throws ball and increases play count.

        Returns:
            A string describing the puppy's play session.
        """
        return self._state.play(self)

    def give_food(self) -> str:
        """
        Puppy gets food and increases feed count.

        Returns:
            A string describing the puppy's feeding session.
        """
        return self._state.feed(self)

    def inc_feeds(self):
        # feed count increases
        self._feeds += 1

    def inc_plays(self):
        # play count increases
        self._plays += 1

    def reset(self):
        # all puppy stats reset
        self._feeds = 0
        self._plays = 0

import puppy_state
import state_eat

class State_Asleep(puppy_state.Puppy_State):
    def feed(self, puppy) -> str:
        """
        Puppy gets fed.

        Args:
            puppy: Puppy gets fed from the state of being asleep.

        Returns:
            A string detailing the feeding session.
        """
        puppy.change_state(state_eat.State_Eat())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        """
        Puppy attempts to play.

        Args:
            puppy: Puppy gets fed from the state of being asleep.

        Returns:
            A string detailing the failed play session.
        """
        puppy.reset()
        return "The puppy is asleep. It doesn't want to play right now."

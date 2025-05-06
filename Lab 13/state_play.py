import puppy_state
import state_asleep

class State_Play(puppy_state.Puppy_State):
    def feed(self, puppy):
        """
        Puppy attempts to be fed.

        Args:
            puppy: Puppy tries to get fed from a state of play.

        Returns:
            A string detailing the failed feeding session.
        """
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """
        Puppy plays from being played.

        Args:
            puppy: Puppy play count increments.

        Returns:
            A string detailing the various play sessions, depending on how exhausted the puppy is.
        """
        # puppy kind of tired
        if puppy._plays == 1:
            puppy.inc_plays()
            return "You throw the ball again and the puppy excitedly chases it."
        elif puppy._plays == 2:     # puppy super tired
            puppy.change_state(state_asleep.State_Asleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it.\
                    \nThe puppy played so much it fell asleep!"

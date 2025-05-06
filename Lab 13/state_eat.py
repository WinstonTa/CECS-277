import puppy_state
import state_asleep
import state_play

class State_Eat(puppy_state.Puppy_State):
    def feed(self, puppy):
        """
        Puppy eats.

        Args:
            puppy : Puppy gets fed or eats so much that it falls asleep.

        Returns:
            A string detailing the eating process.
        """
        if puppy._feeds == 1:
            puppy.inc_feeds()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        elif puppy._feeds == 2:
            puppy.change_state(state_asleep.State_Asleep())
            puppy.reset()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\
                    \nThe puppy ate so much it fell asleep!"

    def play(self, puppy):
        """
        Puppy plays.

        Args:
            puppy : Puppy plays from a state of eating.

        Returns:
            A string detailing the play session.
        """
        puppy.change_state(state_play.State_Play())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."

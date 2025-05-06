import puppy_state
import state_asleep

class State_Play(puppy_state.Puppy_State):
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        if puppy._plays == 1:
            puppy.inc_plays()
            return "You throw the ball again and the puppy excitedly chases it."
        elif puppy._plays == 2:
            puppy.change_state(state_asleep.State_Asleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it.\
                    \nThe puppy played so much it fell asleep!"

import puppy_state
import state_eat

class State_Asleep(puppy_state.Puppy_State):
    def feed(self, puppy):
        puppy.change_state(state_eat.State_Eat())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."

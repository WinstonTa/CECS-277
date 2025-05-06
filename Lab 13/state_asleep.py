import puppy_state

class State_Asleep(puppy_state.Puppy_State):
    def feed(self, puppy):
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."

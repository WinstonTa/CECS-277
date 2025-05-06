import puppy_state

class State_Eat(puppy_state.Puppy_State):
    def feed(self, puppy):
        if puppy._feeds < 2:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\
                    \nThe puppy ate so much it fell asleep!"

    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."

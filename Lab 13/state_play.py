import puppy_state

class State_Play(puppy_state.Puppy_State):
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        if puppy._plays == 0:
            return "The puppy looks up from its food and chases the ball you threw."
        elif puppy.plays == 1:
            return "You throw the ball again and the puppy excitedly chases it.\
                    \nThe puppy played so much it fell asleep!"

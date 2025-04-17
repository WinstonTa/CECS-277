import enemy_factory
import beg_goblin
import beg_troll
import random

class BeginnerEnemyFactory(enemy_factory.EnemyFactory):
    def create_random_enemy(self):
        rand_choice = random.randint(0,1)
        if rand_choice == 0:
            return beg_goblin.BegGoblin()
        else:
            return beg_troll.BegTroll()
        
    


import enemy_factory
import exp_goblin
import exp_troll
import random

class ExpertEnemyFactory(enemy_factory.EnemyFactory):
    # work on this after ExpGoblin and ExpTroll are done
    def create_random_enemy(self):
        rand_choice = random.randint(0,1)
        if rand_choice == 0:
            return exp_goblin.ExpGoblin()
        else:
            return exp_troll.ExpTroll()

    
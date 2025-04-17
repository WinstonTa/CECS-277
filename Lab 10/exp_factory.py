import enemy_factory
import exp_goblin
import exp_troll
import random

class ExpertEnemyFactory(enemy_factory.EnemyFactory):
    # work on this after ExpGoblin and ExpTroll are done
    def create_random_enemy(self):
        rand_choice = random.randint(0,1)
        if rand_choice == 0:
            random_enemy = exp_goblin.ExpGoblin("Grotesque Goblin")
        else:
            random_enemy = exp_troll.ExpTroll("Tyrannical Troll")
        return random_enemy

    
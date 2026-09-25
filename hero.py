import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self,name):
        self.name = name
        self.health = 150
        self.attack_power = 10

    def attack(self):
        return random.randint(1,100)
    
    def take_damage(self,damage):
        if self.health < 0:
            self.health = self.health - (damage * .96)
            return self.health
        def is_alive(self):
            print(self.health)
        


        


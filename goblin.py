import random
from hero import Hero
from enemy import Enemy


class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, 100, 7)
        self.gold = 0

    def stealGold(self, hero):
        """ steal DOUGH """
        print("Gimme the bread")
        self.gold = self.gold + hero.gold
        hero.gold = 0
        print("Lowk got fried*rose*")



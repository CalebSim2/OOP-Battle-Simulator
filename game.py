from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Titanium Castle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")
    hero = Hero("Your Hero Name")
    print(f"The starlight warrior enters with {hero.name} and {hero.health} health")

    goblin = Goblin("Heatseeker")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Heatfinder")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has braved the squable...until")


if __name__ == "__main__":
    main()

boss = Boss("rick")
battle(bob, boss)
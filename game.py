from goblin import Goblin


ARENA_NAME = "The Titanium Castle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Heatseeker")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Heatfinder")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    print("But no hero has braved the squable...until")


if __name__ == "__main__":
    main()

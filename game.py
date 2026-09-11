from goblin import Goblin


ARENA_NAME = "Super cool ARENA"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = Goblin("Steve")
    goblin2 = Goblin("Scrabble")

    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()

from goblin import Goblin
from hero import Hero

ARENA_NAME = "Super cool ARENA"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = Goblin("Steve")
    goblin2 = Goblin("Scrabble")
    hero = Hero("Mr67Man")

    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    hero_attack = hero.attack()
    goblin1.take_damage(hero_attack)


if __name__ == "__main__":
    main()

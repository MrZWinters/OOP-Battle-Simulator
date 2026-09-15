from goblin import Goblin
from heros import Warrior
from Attacks import attack, AOE_attack

ARENA_NAME = "Super cool ARENA"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = Goblin("Steve")
    goblin2 = Goblin("Scrabble")
    hero = Warrior("Mr67Man")

    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    attack(goblin1, hero)
    AOE_attack([goblin1, goblin2], hero)


if __name__ == "__main__":
    main()

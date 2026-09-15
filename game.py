from goblin import Goblin
from heros import Warrior, Mage
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning

ARENA_NAME = "Super cool ARENA"

def battle(hero: Warrior, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive:
        attack(enemy, hero)

        if enemy.is_alive():
            attack(hero,enemy)
    
    if hero.is_alive():
        print(f"{hero.name} wins")
    else:
        print(f"{enemy.name} wins")




def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = Goblin("Steve")
    goblin2 = Goblin("Scrabble")
    goblin3 = Goblin("mark")
    goblin4 = Goblin("sam")
    hero = Warrior("Mr67Man")
    wiz = Mage("MrMage")

    group1 = [goblin1, goblin2]
    group2 = [goblin3, goblin4]

    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    attack(goblin1, hero)
    aoe_attack(group1, hero)

    lightning_orb(goblin3, wiz)
    print(wiz.mp)
    chain_lightning(group2,wiz)
    print(wiz.mp)


    



if __name__ == "__main__":
    main()

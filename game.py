from enemys import Goblin
from heros import Hero
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall
from game_functions import stats, enemy_spawner
import time

ARENA_NAME = "Super cool ARENA"

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    round = 1
    alive_enemys = []
    dead_enemys = []

    print("----------------------------------------------------------------------------")
    hero = Hero(input(f"make character Name: "))
    print("classes: Warrior, Mage")
    clas = str(input("select character class:"))
    if clas.lower() == "warrior":
        hero.max_health
        hero.health = 150
        hero.max_mp = 0
        hero.attack_power = 15
        hero.armor = 15
        hero.weapon = "sword"
    elif clas.lower() == "mage":
        hero.max_health = 120
        hero.health = 120
        hero.max_mp = 100
        hero.mp = 100
        hero.magic_affinity = 1.5
        hero.armor = 6
        hero.weapon = "staff"
    else:
        print("not a class")
    print("----------------------------------------------------------------------------")
    stats(hero)   
    print("----------------------------------------------------------------------------")
    enemy_spawner(round, alive_enemys)
    while alive_enemys != []:
        turn_chose = str(input("attack(a)  items(i)"))
        if turn_chose.lower == "a" or turn_chose.lower == "attack":
            if hero.weapon == "staff":

        elif turn_chose.lower == "i" or turn_chose.lower == "items":
        




    



if __name__ == "__main__":
    main()

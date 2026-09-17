from enemys import Goblin, Boss, Skeleton
from heros import Hero
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall
from game_functions import stats, enemy_spawner, hero_chose_attack, use_items
import time

ARENA_NAME = "Super cool ARENA"

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    round = 1
    alive_enemys = []
    target_list = []
    dead_enemys = []

    print("----------------------------------------------------------------------------")
    hero = Hero(input(f"make character Name: "))
    print("classes: Warrior, Mage")
    clas = str(input("select character class:"))
    if clas.lower() == "warrior":
        hero.max_health
        hero.health = 150
        hero.max_mp = 0
        hero.attack_power = 30
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
    print(f"round: {round}")
    while True:
        while alive_enemys != []:
            turn_chose = str(input("attack(a)  items(i): "))
            if turn_chose == "a" or turn_chose == "attack":
                target_list = alive_enemys
                hero_chose_attack(hero,target_list)     
                print("----------------------------------------------------------------------------")
            elif turn_chose == "i" or turn_chose == "items":
                use_items(hero)

            for enemys in alive_enemys:
                if enemys.is_dead():
                    alive_enemys.pop(alive_enemys.index(enemys))
                    enemys = alive_enemys[0]
        print("----------------------------------------------------------------------------")
        print(f"all enemys are dead")
        print(f"moving on to next round")
        round += 1
        print(f"round: {round}")
            

            
        




    



if __name__ == "__main__":
    main()

from enemys import Goblin, Boss, Skeleton
from heros import Hero
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall
from game_functions import stats, enemy_spawner, hero_chose_attack, use_items, enemy_chose_attack, shop, check_levelup, levelup
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
    print("classes: Warrior(w), Mage(m)")
    clas = str(input("select character class:"))
    if clas.lower() == "w":
        hero.max_health = 150
        hero.health = 150
        hero.max_mp = 0
        hero.attack_power = 150
        hero.armor = 2
        hero.weapon = "sword"
    elif clas.lower() == "m":
        hero.max_health = 120
        hero.health = 120
        hero.max_mp = 100
        hero.mp = 100
        hero.magic_affinity = 1.5
        hero.armor = 1.3
        hero.weapon = "staff"
    else:
        print("not a class")
    print("----------------------------------------------------------------------------")
    stats(hero)   
    print("----------------------------------------------------------------------------")
    print(f"round: {round}")
    enemy_spawner(round, alive_enemys)
    while hero.health != 0:
        while alive_enemys != []:
            turn_chose = str(input("attack(a)  items(i)  skip(anything else): "))
            if turn_chose == "a" or turn_chose == "attack":
                target_list = alive_enemys
                hero_chose_attack(hero,target_list)     
                print("----------------------------------------------------------------------------")
            elif turn_chose == "i" or turn_chose == "items":
                use_items(hero)
            else:
                print("turn skipped")   
                print("----------------------------------------------------------------------------")             

            for enemy in alive_enemys:
                enemy_chose_attack(hero, enemy)
                print("----------------------------------------------------------------------------")

            for enemy in alive_enemys:
                if enemy.is_dead(hero):
                    alive_enemys.pop(alive_enemys.index(enemy))
            for enemy in alive_enemys:
                if enemy.is_dead(hero):
                    alive_enemys.pop(alive_enemys.index(enemy))
                    
        print("----------------------------------------------------------------------------")
        print(f"all enemys are dead")
        need_levelup = check_levelup(hero)
        print(hero.xp)
        if need_levelup == True:
            levelup(hero)
        after_round = str(input("shop(s)  next round(n)"))
        if after_round == "s" or after_round == "shop":
            shop(hero)
        elif after_round == "n" or after_round == "next round":
            print(f"moving on to next round")
            print("----------------------------------------------------------------------------")
            round += 1
            print(f"round: {round}")
            enemy_spawner(round, alive_enemys)
            print("----------------------------------------------------------------------------")
    print("you died")

            

            
        


if __name__ == "__main__":
    main()

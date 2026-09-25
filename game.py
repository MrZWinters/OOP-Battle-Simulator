from heros import Hero
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
    time.sleep(0.5)
    # player picks name and class
    hero = Hero(input(f"make character Name: "))
    print("classes: Warrior(w), Mage(m)")
    clas = str(input("select character class:"))
    #sets the players stats to match the class they picked
    if clas.lower() == "w":
        hero.max_health = 150
        hero.health = 150
        hero.max_mp = 0
        hero.attack_power = 20
        hero.armor = 1.7
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
    #shows the players stats
    time.sleep(0.5)
    stats(hero)   
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    print(f"round: {round}")
    #spawns the first round of enemys
    enemy_spawner(round, alive_enemys)
    #battle loop
    while hero.health != 0:
        while alive_enemys != [] and hero.health != 0:
            turn_chose = str(input("attack(a)  items(i)  skip(anything else): "))
            #lets the player attack
            if turn_chose == "a" or turn_chose == "attack":
                target_list = alive_enemys
                hero_chose_attack(hero,target_list)     
                print("----------------------------------------------------------------------------")
                time.sleep(0.5)
            #lets the player select and item
            elif turn_chose == "i" or turn_chose == "items":
                use_items(hero)
            #skips turn
            else:
                print("turn skipped")   
                print("----------------------------------------------------------------------------")
                time.sleep(0.5)          

            #checks if the enemys are dead
            for enemy in alive_enemys:
                if enemy.is_dead(hero):
                    alive_enemys.pop(alive_enemys.index(enemy))
            for enemy in alive_enemys:
                if enemy.is_dead(hero):
                    alive_enemys.pop(alive_enemys.index(enemy))

            #has each enemy attack the player out of a select amount of attacks
            for enemy in alive_enemys:
                enemy_chose_attack(hero, enemy)
                hero.is_dead()
                print("----------------------------------------------------------------------------")
                time.sleep(0.5)

            
        #end of round loop          
        print("----------------------------------------------------------------------------")
        time.sleep(0.5)
        print(f"all enemys are dead")
        #checks if the player can level up
        need_levelup = check_levelup(hero)
        while need_levelup == True:
            levelup(hero)
            need_levelup = check_levelup
        #gets the players after round input
        after_round = str(input("shop(s)  next round(n)"))
        #brings player to the shop
        if after_round == "s" or after_round == "shop":
            shop(hero)
        #brings the player to the next round
        elif after_round == "n" or after_round == "next round":
            #spawns more enemys for the next round
            print(f"moving on to next round")
            print("----------------------------------------------------------------------------")
            time.sleep(0.5)
            round += 1
            print(f"round: {round}")
            enemy_spawner(round, alive_enemys)
            print("----------------------------------------------------------------------------")
            time.sleep(0.5)
    print("you died")

            

            
        


if __name__ == "__main__":
    main()

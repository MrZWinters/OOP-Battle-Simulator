import random
from heros import Hero
from enemys import Goblin, Skeleton, Boss
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall 
from enemy_attacks import attack_scratch, attack_punch, attack_slash
import time

def rand_name():
    namelist = ["James", "John", "Robert", "Michael", "William", "David", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Alexander", "Patrick", "Frank", "Raymond", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary", "Kyle", "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Christian", "Roger", "Noah", "Gerald", "Carl", "Terry", "Sean", "Austin", "Arthur", "Lawrence", "Jesse", "Dylan", "Jordan", "Bryan", "Billy", "Joe", "Bruce", "Gabriel", "Albert", "Logan", "Alan", "Juan", "Wayne", "Roy", "Ralph", "Eugene", "Randy", "Vincent", "Russell", "Louis", "Philip", "Bobby", "Johnny", "Bradley", "Mason", "Philip", "Connor", "Cameron", "Eli", "Isaac"]
    return(namelist[random.randint(1,100)])

def stats(hero: Hero):
    '''Prints a Stat Sheet'''
    print(f"Level {hero.level}")
    print(f"Health:{hero.health}")
    print(f"MP:{hero.mp}")
    print(f"Attack Power:{hero.attack_power}")
    print(f"Magic Affinity:{hero.magic_affinity}")
    print(f"Armor:{hero.armor}")
    print(f"Coins:{hero.coins}")

def enemy_spawner(round: int, aliveEnemys: list):
    if round % 10 == 0:
        #spawns a boss
        aliveEnemys.append(Boss(rand_name()))
        print(f"a boss spawns")
    elif round % 3 == 0:
        #spawns multiple enemys every 3 rounds
        for i in range(random.randint(3,3)):
            aliveEnemys.append(Goblin(rand_name()))
        print(f"{len(aliveEnemys)} goblins spawn")
    else:
        #spawns an enemy
        aliveEnemys.append(Goblin(rand_name()))
        print(f"a goblin spawns")

def hero_chose_attack(hero: Hero, alive_enemys: list,):
    if hero.weapon == "sword":
        attack_chose = str(input("slash(s)  AOE slash(a)"))
        if attack_chose == "s" or attack_chose == "slash":
            if len(alive_enemys) > 1:
                print("targest:")
                for enemys in alive_enemys:
                    print(f"{alive_enemys.index(enemys)+1}: {alive_enemys[alive_enemys.index(enemys)].name}")
                target = int(input("select enemy(number): "))
                attack(alive_enemys[target-1], hero)
            else:
                attack(alive_enemys[0], hero)
        elif attack_chose == "a" or attack_chose == "AOE slash":
            aoe_attack(alive_enemys, hero)
    elif hero.weapon == "staff":
        attack_chose = str(input("spell(s)  AOE spell(a)"))
        if attack_chose == "s" or attack_chose == "spell":
            spell = str(input("chose a spell: Lightning_orb(l), Fireball(f)"))
            if spell == "l" or spell == "lightning orb":
                if len(alive_enemys) > 1:
                    print("targest:")
                    for enemys in alive_enemys:
                        print(f"{alive_enemys.index(enemys)+1}: {alive_enemys[alive_enemys.index(enemys)].name}")
                    target = int(input("select enemy(number): "))
                    lightning_orb(alive_enemys[target-1], hero)
                else:
                    lightning_orb(alive_enemys[0], hero)
            elif spell == "f" or spell == "fireball":
                if len(alive_enemys) > 1:
                    print("targest:")
                    for enemys in alive_enemys:
                        print(f"{alive_enemys.index(enemys)+1}: {alive_enemys[alive_enemys.index(enemys)].name}")
                    target = int(input("select enemy(number): "))
                    fireball(alive_enemys[target-1], hero)
                else:
                    fireball(alive_enemys[0], hero)
        elif attack_chose == "a" or attack_chose == "aoe spell":
            spell = str(input("chose a spell: Chain Lightning(l), Firewall(f)"))
            if spell == "l" or spell == "chain lightning":
                chain_lightning(alive_enemys, hero)
            if spell == "f" or spell == "firewall":
                firewall(alive_enemys, hero)

def enemy_chose_attack(hero: Hero, enemy: Goblin):
    rand_attack = random.randint(1,100)
    if enemy.statis_effect == "burn":
        enemy.take_damage(5)
    if enemy.statis_effect != "stun":
        if rand_attack >= 1 and rand_attack <= 33:
            attack_scratch(hero, enemy)
        elif rand_attack >= 34 and rand_attack <= 66:
            attack_punch(hero, enemy)
        elif rand_attack >= 67 and rand_attack <= 99:
            attack_slash(hero, enemy)
        elif rand_attack == 100:
            print(f"{enemy.name} trys to attack and falls on its face")

def shop(hero: Hero):
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    print("---can only buy one item---")
    print("shop items: ")
    print(f"coins: {hero.coins}")
    print("healing potion(h): 8")
    print("mana potion(m): 8")
    print("upgrade armor(a): 30")
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    shop_chose = str(input("purchase: "))

    if shop_chose == "h" or shop_chose == "healing potion":
        if hero.coins >= 8:
            print(f"{hero.name} bought a healing potion")
            hero.items.append("healing potion")
            hero.coins -= 8
        else:
            print("your poor")

    if shop_chose == "m" or shop_chose == "mana potion":
        if hero.coins >= 8:
            print(f"{hero.name} bought a mana potion")
            hero.items.append("mana potion")
            hero.coins -= 8
        else:
            print("your poor")

    if shop_chose == "a" or shop_chose == "upgrade armor":
            if hero.coins >= 30:
                print(f"{hero.name} bought an armor upgrade")
                hero.armor += 0.1
                hero.coins -= 30
            else:
                print("your poor")

def use_items(hero: Hero):
    items = hero.items
    print("items:")
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    if items == []:
        print("you have no items")
        print("----------------------------------------------------------------------------")
        time.sleep(0.5)          
    else:
        for item in items:
            print(f"{items.index(item)+1}: ({item})")
        print("----------------------------------------------------------------------------")
        time.sleep(0.5)
        selected_item = int(input("selects item number: "))-1
        if items[selected_item] == "healing potion":
            hero.health = max(hero.max_health, (hero.health + 50))
            print(f"{hero.name} healed to {hero.health}")
            hero.items.pop(selected_item - 1)
            print("----------------------------------------------------------------------------")
            time.sleep(0.5)          
        elif items[selected_item] == "mana potion":
            hero.mp = max(hero.max_mp, (hero.mp + 80))
            print(f"{hero.name} restored mana to {hero.mp}")
            print("----------------------------------------------------------------------------")
            time.sleep(0.5)          

def check_levelup(hero: Hero):
    need_levelup = False
    if int(hero.xp) >= int(66 * (1.5 * hero.level)):
        need_levelup = True
    return need_levelup

def levelup(hero: Hero):
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    print("you have a level up")
    print(f"max health(h): {hero.max_health}")
    print(f"max mana(m): {hero.max_mp}")
    print(f"attack power(p): {hero.attack_power}")
    print(f"magic affinity(a): {hero.magic_affinity}")
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
    levelchose = str(input("select stat to level up: "))
    if levelchose == "h" or levelchose == "max health":
        hero.max_health += 50
        hero.xp -= int((66 * (1.5 * hero.level)))
        print(f"max health is now: {hero.max_health}")
    elif levelchose == "m" or levelchose == "max mana":
        hero.max_mp += 50
        hero.xp -= int((66 * (1.5 * hero.level)))
        print(f"max mana is now: {hero.max_mp}")
    elif levelchose == "p" or levelchose == "attack power":
        hero.attack_power += 5
        hero.xp -= int((66 * (1.5 * hero.level)))
        print(f"attack power is now: {hero.attack_power}")
    elif levelchose == "a" or levelchose == "magic affinity":
        hero.magic_affinity += 0.1
        hero.xp -= int((66 * (1.5 * hero.level)))
        print(f"magic affinity is now: {hero.magic_affinity}")
    print("----------------------------------------------------------------------------")
    time.sleep(0.5)
import random
from heros import Hero
from enemys import Goblin, Skeleton, Boss
from Attacks import attack, aoe_attack, lightning_orb, chain_lightning, fireball, firewall 

def rand_name():
    namelist = ["James", "John", "Robert", "Michael", "William", "David", "Joseph", "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Mark", "Donald", "Steven", "Paul", "Andrew", "Joshua", "Kenneth", "Kevin", "Brian", "George", "Timothy", "Ronald", "Edward", "Jason", "Jeffrey", "Ryan", "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon", "Benjamin", "Samuel", "Gregory", "Alexander", "Patrick", "Frank", "Raymond", "Jack", "Dennis", "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary", "Kyle", "Walter", "Ethan", "Jeremy", "Harold", "Keith", "Christian", "Roger", "Noah", "Gerald", "Carl", "Terry", "Sean", "Austin", "Arthur", "Lawrence", "Jesse", "Dylan", "Jordan", "Bryan", "Billy", "Joe", "Bruce", "Gabriel", "Albert", "Logan", "Alan", "Juan", "Wayne", "Roy", "Ralph", "Eugene", "Randy", "Vincent", "Russell", "Louis", "Philip", "Bobby", "Johnny", "Bradley", "Mason", "Philip", "Connor", "Cameron", "Eli", "Isaac"]
    return(namelist[random.randint(1,100)])

def stats(hero: Hero):
    '''Prints a Stat Sheet'''
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

            
def use_items(hero: Hero):
    items = hero.items
    print("items:")
    print("----------------------------------------------------------------------------")
    for item in items:
        print(f"{items.index(item)+1}: ({item})")
    print("----------------------------------------------------------------------------")
    selected_item = int(input("selects item number: "))-1
    # if items[selected_item] == "apple":
        
    # elif items[selected_item] == "bannana":
        
    # elif items[selected_item] == "orange":
        
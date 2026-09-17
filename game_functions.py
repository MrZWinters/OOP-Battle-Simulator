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
        for i in range(random.randint(2,3)):
            aliveEnemys.append(Goblin(rand_name()))
        print(f"{i} goblins spawn")
    else:
        #spawns an enemy
        aliveEnemys.append(Goblin(rand_name()))
        print(f"a goblin spawns")

def hero_attack_chose(hero: Hero, alive_enemys: list, chose):
    if hero.weapon == "sword":
        attack_chose = str(input("slash(s)  AOE slash(a)"))
        if attack_chose.lower == "s" or attack_chose.lower == "slash":
            if len(alive_enemys) >= 1:
                print("targest:")
                for enemys in alive_enemys:
                    print(f"{enemys+1}: {alive_enemys(enemys).name}")
                target = (input("select enemy(number): "))
                attack(alive_enemys(target-1), hero)
            else:
                attack(alive_enemys(0), hero)
            
        elif attack_chose.lower == "a" or attack_chose.lower == "AOE slash":
            aoe_attack(alive_enemys, hero)
    elif 


        
#def shop():


#def items():





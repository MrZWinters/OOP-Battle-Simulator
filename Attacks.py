def attack(target, attacker):
    print(f"{attacker.name} attacks {target.name}")
    target.take_damage(max(0, attacker.attack() - target.armor))

def aoe_attack(target_list, attacker):
    global attack
    if attacker.canAOE == True:
        print(f"{attacker.name} does an AOE attack")
        for attacked in target_list:
            attack(attacked,attacker)
    else:
        print(f"{attacker.name} tryed to do an AOE attack and failed")
        attacker.health -= 1
        print(f"{attacker.name} took 1 damage and is now at {attacker.health}")


def lightning_orb(target, attacker):
    if attacker.magic_affinity == 0:
        print(f"{attacker.name} has no magic affinity")
    elif attacker.mp == 0:
        print(f"{attacker.name} has no mp left")
    else:
        print(f"{attacker.name} casts ballLightning at {target.name}")
        target.take_damage(max(0,int(20 * attacker.magic_affinity)))
        target.statis_effect = "stun"
        print(f"{target.name} was stuned")
        attacker.mp -= 10

def chain_lightning(target_list, attacker):
    if attacker.magic_affinity == 0:
        print(f"{attacker.name} has no magic affinity")
    elif attacker.mp == 0:
        print(f"{attacker.name} has no mp left")
    elif attacker.canAOE == True:
        for attacked in target_list:
            print(f"{attacker.name} casts chainlightning and hits {attacked.name}")
            attacked.take_damage(max(0,int(20 * attacker.magic_affinity)))
            attacked.statis_effect = "stun"
            print(f"{attacked.name} was stuned")
            attacker.mp -= 20
    else:
        print(f"{attacker.name} cant use that spell")


def fireball(target, attacker):
    if attacker.magic_affinity == 0:
        print(f"{attacker.name} has no magic affinity")
    elif attacker.mp == 0:
        print(f"{attacker.name} has no mp left")
    else:
        print(f"{attacker.name} casts fireball at {target.name}")
        target.take_damage(max(0,int(20 * attacker.magic_affinity)))
        target.statis_effect = "burn"
        print(f"{target.name} was burned")
        attacker.mp -= 10

def firewall(target_list, attacker):
    if attacker.magic_affinity == 0:
        print(f"{attacker.name} has no magic affinity")
    elif attacker.mp == 0:
        print(f"{attacker.name} has no mp left")
    elif attacker.canAOE == True:
        for attacked in target_list:
            print(f"{attacker.name} casts chainlightning and hits {attacked.name}")
            attacked.take_damage(max(0,int(20 * attacker.magic_affinity)))
            attacked.statis_effect = "burn"
            print(f"{attacked.name} was burned")
            attacker.mp -= 20
    else:
        print(f"{attacker.name} cant use that spell")
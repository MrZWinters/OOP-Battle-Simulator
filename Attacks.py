def attack(target, attacker):
    print(f"{attacker.name} attacks {target.name}")
    target.take_damage(max(0, attacker.attack() - target.armor))

def AOE_attack(target_list, attacker):
    global attack
    if attacker.canAOE == True:
        print(f"{attacker.name} does an AOE attack")
        for attacked in target_list:
            attack(attacked,attacker)
    else:
        print(f"{attacker.name} tryed to do an AOE attack and failed")
        attacker.health -= 1
        print(f"{attacker.name} took 1 damage and is now at {attacker.health}")



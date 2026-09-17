def attack_scratch(target, attacker):
    print(f"{attacker.name} scratches at {target.name}")
    target.take_damage(max(0, int((attacker.attack()/2) / target.armor)))

def attack_punch(target, attacker):
    print(f"{attacker.name} pucnhes at {target.name}")
    target.take_damage(max(0, int((attacker.attack()/1.5) / target.armor)))

def attack_slash(target, attacker):
    print(f"{attacker.name} slashes at {target.name}")
    target.take_damage(max(0, int((attacker.attack()/1) / target.armor)))


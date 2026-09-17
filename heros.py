import random

class Hero:
    def __init__(self, name):
            self.name = name
            self.max_health = 100
            self.health = 100
            self.max_mp = 0
            self.mp = 0
            self.attack_power = 5
            self.magic_affinity = 0
            self.armor = 1
            self.canAOE = True
            self.weapon = "none"
            self.coins = 0
            self.statis_effect = "none"
            self.items =[]
        
    def attack(self):
        """Return a random amount of damage."""
        return random.randint(20, self.attack_power)
        
    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        
    def is_dead(self):
        """Return True if dead."""
        dead = False
        if self.health == 0:
            dead = True
        return dead
        
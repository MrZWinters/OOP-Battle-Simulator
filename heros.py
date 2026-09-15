import random

class Warrior:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = int(random.randint(100,150))
        self.attack_power = 25
        self.magic_affinity = 0
        self.armor = 10
        self.mp = 0
        self.canAOE = True

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(10, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0

class Mage:

    def __init__(self, name):
        self.name = name
        self.health = int(random.randint(100,120))
        self.attack_power = 5
        self.magic_affinity = 1.5
        self.armor = 10
        self.mp = 100
        self.canAOE = True
    
    def attack(self):
            """Return a random amount of damage."""
            return random.randint(10, self.attack_power)
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    
    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0


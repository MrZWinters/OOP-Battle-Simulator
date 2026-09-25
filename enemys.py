import random
from heros import Hero

class enemy:
    def attack(self):
        """Return a random amount of damage."""
        return max(1, random.randint((self.attack_power-10), self.attack_power))

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self, hero: Hero):
        """Return True if dead."""
        dead = False
        if self.health == 0:
            print(f"{hero.name} got 10 coins and 50 xp")
            hero.coins += 10
            hero.xp += 50
            dead = True
        return dead

class Goblin(enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.magic_affinity = 0
        self.armor = 1
        self.mp = 0
        self.canAOE = False
        self.statis_effect = "none"

class Boss(enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = 35
        self.magic_affinity = 0
        self.armor = 1.5
        self.mp = 0
        self.canAOE = True
        self.statis_effect = "none"

        def attack(self):
            return super().attack() + 5


class Skeleton(enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 25
        self.magic_affinity = 0
        self.armor = 1
        self.mp = 0
        self.canAOE = False
        self.statis_effect = "none"
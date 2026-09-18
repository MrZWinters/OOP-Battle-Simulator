import random
from heros import Hero


class Goblin:
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

class Boss:
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
        """Return a random amount of damage."""
        return max(1, random.randint((self.attack_power-5), self.attack_power))

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self, hero: Hero):
        """Return True if dead."""
        dead = False
        if self.health == 0:
            print(f"{hero.name} got 20 coins and 100 xp")
            hero.coins += 20
            hero.xp += 100
            dead = True
        return dead

class Skeleton:
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

    def attack(self):
        """Return a random amount of damage."""
        return max(1, random.randint((self.attack_power-5), self.attack_power))

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self, hero: Hero):
        """Return True if dead."""
        dead = False
        if self.health == 0:
            print(f"{hero.name} got 15 coins and 70 xp")
            hero.coins += 15
            hero.xp += 70
            dead = True
        return dead
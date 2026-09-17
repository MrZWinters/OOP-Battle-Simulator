import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.magic_affinity = 0
        self.armor = 0
        self.mp = 0
        self.canAOE = False
        self.statis_effect = "none"

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self):
        """Return True if dead."""
        if self.health <= 0:
            return True
        else:
            return False

class Boss:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 250
        self.attack_power = 20
        self.magic_affinity = 0
        self.armor = 10
        self.mp = 0
        self.canAOE = True
        self.statis_effect = "none"

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self):
        """Return True if dead."""
        if self.health <= 0:
            return True
        else:
            return False

class Skeleton:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.magic_affinity = 0
        self.armor = 0
        self.mp = 0
        self.canAOE = False
        self.statis_effect = "none"

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {int(damage)} damage. Health: {int(self.health)}")

    def is_dead(self):
        """Return True if dead."""
        dead = False
        if self.health == 0:
            dead = True
        return dead
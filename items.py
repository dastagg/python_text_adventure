class Weapon:
    """docstring for Weapon"""

    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    """docstring for Rock"""

    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    """docstring for Dagger"""

    def __init__(self):
        self.name = "Dagger"
        self.description = (
            "A small dagger with some rust. " "Somewhat more dangerous than a rock."
        )
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    """docstring for RustySword"""

    def __init__(self):
        self.name = "Rusty sword"
        self.description = (
            "This sword is showing its age, " "but still has some fight in it."
        )
        self.damage = 20
        self.value = 100


class Consumable:
    """docstring for Consumable"""

    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return f"{self.name} (+{self.healing_value} HP)"


class CrustyBread(Consumable):
    """docstring for CrustyBread"""

    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    """docstring for HealingPotion"""

    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60

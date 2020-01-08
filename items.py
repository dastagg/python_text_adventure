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


class Dagger(Weapon):
    """docstring for Dagger"""

    def __init__(self):
        self.name = "Dagger"
        self.description = (
            "A small dagger with some rust. Somewhat more dangerous than a rock."
        )
        self.damage = 10


class RustySword(Weapon):
    """docstring for RustySword"""

    def __init__(self):
        self.name = "Rusty sword"
        self.description = (
            "This sword is showing its age, but still has some fight in it."
        )
        self.damage = 20

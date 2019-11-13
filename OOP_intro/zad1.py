class Dog:
    def __init__(self, name, color, breed):
        self.name = name
        self.breed = breed
        self.color = color

    def bark(self):
        return "hau "
    def wave(self):
        return "macham ogonem ~~~~~~******~~~~~~"

obj_lab = Dog("Xander", "White", "Labrador")
obj_ter = Dog("Stefan", "Black", "Terrier")

print(obj_lab.wave())
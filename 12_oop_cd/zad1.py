class Animals:
    def __init__(self, name):
        print("Zwierzęta")


class Mammals(Animals):
    def __init__(self):
        return "SSAK"

class Human(Mammals, Animals):
    def __init__(self):
        return "Czlowiek"


class Dog(Mammals, Animals):
    def __init__(self):
        return "Pies"

class Cat(Mammals, Animals):
    def __init__(self):
        return "Kot"
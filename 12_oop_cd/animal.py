class Vertebrate:
    backbone = True

    def __init__(self):
        print("Szkielet wewnętrzny kręgowców...")

    def desc(self):
        print("Zewnętrzna pokrywe ciala kregowcow stanowi skora")





    # def __str__(self):
    #     return "I'm Vertebrate"

class Cat(Vertebrate):
    def __init__(self,name):
        print("I'm cat")
        self.name = name

    def desc(self):
        print("Koty sa super!")
        super().desc()
    #   super().__init__  powrot do modulu init

ver = Vertebrate()
kitty = Cat("Kitty")


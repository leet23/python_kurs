# dog = {
#     name: "Piesek";
#     breed: "Labrador";
#     age: 6;
#     color: "white";
# }
# obj_pimpek.name = "Pimpek"
# obj_pimpek.breed = "Labrador"
# obj_pimpek.age = 6
# obj_pimpek.color = "white"
import random
class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def pseudo(self):
        adj = ["Destroyer", "Psycho", "Sweet", "Funny"]
        return self.name + "-" + random.choice(adj)
    def bark(self):
        return "hau " * self.age

obj_pimpek = Dog("Pimpek", "Labrador", 6, "White")
obj_dyzio = Dog("Dyzio", "Terrier", 3, "Black")


print(obj_pimpek.name)
print(obj_pimpek.color)
print(Dog.pseudo(obj_pimpek))
print(obj_pimpek.pseudo())
print(obj_dyzio.pseudo())
print(obj_dyzio.bark())
print(obj_pimpek.bark())
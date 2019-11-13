class Fifo:
    def __init__(self, elements):
        self.elements = elements

    def __str__(self):
        return "-".join(self.elements)

    # def show(self):
    #     print(self.elements)

    def get(self):
        if len(self.elements) == 0
            return "brak elementow"
        else:
            return self.elements.pop(0)

    def put(self):
        value = input("Podaj element:")
        self.elements.append(value)
        return "Dodano!"



list_elem = ['a', 'b', 'c', 'd']
fifo1= Fifo(list_elem)
print(fifo1)
print(fifo1.get())
print(fifo1)

class Necromorph:
    def __init__(self, type, danger_level, weakness):
        self.type = type
        self.danger_level = danger_level
        self.weakness = weakness
    def revealnecro(self):
        print(f"This necromorph is type {self.type} and the danger level is {self.danger_level}. The weakness of this necromorph is {self.weakness}")
slasher = Necromorph("Light",1,"Limbs")
slasher.revealnecro()
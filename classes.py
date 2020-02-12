# Parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {} \nSpecies: {} \nLegs: {} \nArms: \nDNA: {} \nOrigin: \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = "Miles"
    species = "Homosapien"
    legs = 2
    arms = 2
    orgin = "earth"

    def ingenuity(self):
        msg = "\nSuper intelligence"
        return msg

# child class dog
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nSuper bite"
        return msg

# child class bachterium
class Bachterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    orgin = "Mars"

    def replication(self):
        msg = "\nSplits itself into two bodies"
        return msg

    

if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bachteria = Bachterium()
    print(bachteria.information())
    print(bachteria.replication())
    

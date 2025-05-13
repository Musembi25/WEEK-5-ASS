# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}. My power is {self.power}."

    def fight_crime(self):
        return f"{self.name} uses {self.power} to fight crime!"

# Subclass - with encapsulation
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.__gadgets = gadgets  # encapsulated attribute

    def reveal_gadgets(self):
        return f"{self.name}'s gadgets: {', '.join(self.__gadgets)}"

    def fight_crime(self):
        return f"{self.name} uses advanced tech and {self.power} to save the day!"

# Subclass - another superhero type
class MysticHero(Superhero):
    def __init__(self, name, power, origin, spell_book):
        super().__init__(name, power, origin)
        self.spell_book = spell_book

    def cast_spell(self):
        return f"{self.name} casts a powerful spell from the {self.spell_book}!"

# Testing the class
hero1 = TechHero("Gadgetman", "Tech Manipulation", "Silicon City", ["Laser Pen", "Drone Suit"])
hero2 = MysticHero("Mystra", "Elemental Magic", "Ancient Realm", "Book of Eternity")

print(hero1.introduce())
print(hero1.fight_crime())
print(hero1.reveal_gadgets())

print(hero2.introduce())
print(hero2.fight_crime())
print(hero2.cast_spell())

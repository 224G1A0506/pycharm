class Superhero:
    def __init__(self,name,power,city):
        self.name=name
        self.power=power
        self.city=city
    def introduce(self):
        print(f"I am {self.name}! I protect {self.city} with my power of {self.power}.")

    def changeCity(self, new_city):
        self.city = new_city      # Change the hero's city
        print(f"{self.name} has moved to {self.city}!")

        
hero=Superhero("arif",123,"atp")
hero.introduce()
hero.changeCity("banglore")

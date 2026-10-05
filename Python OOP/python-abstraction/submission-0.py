class Superhero:
    def __init__(self, name: str):
       self._name = name
       self._power_level = 40

    def enough_power_level_to_fly(self):
        if self._power_level < 20:
            return True
        else:
            return False

    def fly(self):
        if self.enough_power_level_to_fly():
            return "Too tired to fly..."
        else:
            self._power_level -= 20
            return "Up up and away!"


    
# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  

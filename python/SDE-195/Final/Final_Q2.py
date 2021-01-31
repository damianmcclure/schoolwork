class Character:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def heal(self):
        self.health = self.health+2

    def takehit(self, amount):
        self.health = self.health-amount

    def attack(self, character):
        character.takehit(self.strength)

Dragon = Character(10, 4)
Troll = Character(12, 3)

Dragon.attack(Troll)
Troll.heal()
print(Troll.health)

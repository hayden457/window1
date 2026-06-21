class AnimalCard:
    
    def __init__(self, name, power, maxhealth):
        self.name = name
        self.power = power
        self.maxhealth = maxhealth
        self.health = maxhealth
    
    def show(self):
        print (self.name)
    
    def strike(self, other):
        other.health = self.power
        print("{} strikes {}, doing {} damage!".format(
            self.name,
            other.name,
            self.power))
        if other.health <= 0:
            other.health = 0
            print (other.name,"has faint!")
            return True
        else:
            print ("{}'s health: {}/{}".format(
                other.name,
                other.health,
                other.maxhealth))
            return False
        
    def fight(self, other):
        print(f"{} is battling {}!")
        other.strike(self)
        self.strike(other)
        for animal.health 
    

chicken = AnimalCard("Chicken", 2, 4)
snake = AnimalCard("Snake", 3, 2)

print("Initial Stats:")
chicken.show()
snake.show()

print("\nBattle Begins!")
chicken.strike(snake)
snake.strike(chicken)

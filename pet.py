#Create a class called Pet with the following:

#Attributes:
#name: the name of your pet
#hunger: an integer representing hunger level (0 = full, 10 = very hungry)
#energy: an integer representing energy level (0 = tired, 10 = fully rested)
#happiness: an integer (0–10)

#Methods:
#eat(): reduces hunger by 3 points (but not below 0), and increases happiness by 1.
#sleep(): increases energy by 5 points (but not above 10).
#play(): decreases energy by 2, increases happiness by 2, and increases hunger by 1.
#get_status(): prints the current state of the pet.

#Pet class definition
class Pet:
    #constructor to initialise attributes
    def __init__(self, name, hunger, energy, happiness): 
        self.name = name
        self.hunger = hunger 
        self.energy = energy
        self.happiness = happiness

    #eat() method definition 
    def eat(self):
        while int(self.hunger) >= 0:
            self.hunger = self.hunger -3
            self.happiness = self.happiness + 1
            print("Hunger: " + self.hunger + "\n" + "Happiness: " + self.happiness + '\n')

        #if hunger >= 0:
        #    hunger = hunger -3
        #    happiness = happiness +1
        #    print("Hunger: " + hunger + "\n" + "Happiness: " + happiness)
        #else:
        #    print("Hunger is below zero. Pet is dead. You cant feed dead pet. :/")

    #sleep() function definition
    def sleep(self):
        while int(self.energy) <=10:
            self.energy = self.energy + 5
            print("Energy: " , self.energy ,'\n')
    
    #play() method definition
    def play(self):
        self.energy = self.energy - 2
        self.happiness = self.happiness  + 2
        self.hunger = self.hunger - 1
    
    #get_status() method definition
    def get_status(self):
        print("Pet state: " )
        print("name:", self.name)
        print("hunger:" , self.hunger)
        print("energy:" , self.energy)
        print("happiness:", self.happiness)    


#Bonus 🎯
#Add a method train(trick) that teaches your pet a new trick and stores it in a list.
#Add a method show_tricks() that prints all learned tricks.
import pet

#defining variables
name = input("Enter the pets name: ")
hungry = input("How hungry is your pet? Enter value from 0 to 10?: ")
energy = input("How energetic is pet? Enter value from 0 to 10)?: ")
happiness = input("How happy is your pet? Enter value from 0 to 10: ")

#creating pet objects
p = pet(name,hungry,energy,happiness)
p.eat()
p.play()
p.sleep()
p.get_status()
 
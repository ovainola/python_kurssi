# -*- coding: utf-8 -*-
 
# Esimerkkiä yrittää näyttää, kuinka perintä toimii pythonissa class:eilla

# Luodaan pääluokka: Eläin
class Animal(object):
    
    def __init__(self, species, sound, attack_method):
        self.species = species
        self.sound = sound
        self.attack_method = attack_method
    
    def animal_says(self):
        print("{0} says {1}".format(self.species, self.sound))
        
    def attack(self):        
        print("%s: %s" % (self.species, self.attack_method))        

# Subluokka: kissa
class Cat(Animal):
    
    def __init__(self, name, age):
        super(Cat, self).__init__("Cat", "Miau", "Scratch")
        self.name = name
        self.age = age

    def purr(self):
        print("Cat begins to purr")
     
# Subluokka: koira
class Dog(Animal):
    
    def __init__(self, name, age):
        super(Dog, self).__init__("Dog", "Wuh", "Bite")
        self.name = name
        self.age = age
    
    def play(self, item):
        print("Dog begins to play with: %s" % item)

# Subluokka: lehmä
class Cow(Animal):
    
    def __init__(self, name, age):
        super(Cow, self).__init__("Cow", "Muu", "Impale")
        self.name = name
        self.age = age

    def milk_mode(self):
        print("Milk mode initiated! Beginning brewing process")

# Samat temput voisi myös tehdä yhdellä luokalla
class MasterAnimal(object):
    
    def __init__(self, species, sound, name, age, attack_method):
        self.species = species
        self.sound = sound
        self.name = name
        self.age = age
        self.attack_method = attack_method
    
    def animal_says(self):
        print("{0} says {1}".format(self.species, self.sound))
        
    def attack(self):
        print("%s %s" % (self.species, self.attack_method))

# Esimerkin tarkoituksena on näyttää, että olioita voidaan tehdä monella tapaa
# Joskus on kuitenkin suotavaa tehdä pääluokkia (Base class) ja sivuluokia
# (Sub class) jotta voidaan pilkkoa rakennetta helpommin hallittavaksi.

if __name__ == '__main__':
    mirri = Cat("Mirri", 1)
    mansikki = Cow("Mansikki", 5)
    musti = Dog("Musti", 4)
    
    
    mirri.animal_says()
    mansikki.animal_says()
    musti.animal_says()
    
    mirri.attack()
    mansikki.attack()
    musti.attack()
    
    mirri.purr()
    mansikki.milk_mode()
    musti.play("ball")
    
    master_animal = MasterAnimal("sloath", "ngghhh", "mike", "24", "play dead")
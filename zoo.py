# Zoo (Optional) Python OOP
# Erin Winking

import random

all_animals = []
class Zoo:
    def __init__(self, zooname):
        zoo_name = zooname
        print(f"Zoo named {zoo_name} created!!")

    def feed(self):
        randhealth = random.randrange(1, 25)
        randhappy = random.randrange(1, 10)
        self.health += randhealth
        self.happiness += randhappy
        newhealth = self.health
        newhappiness = self.happiness
        for animals in all_animals:
            if animals["name"] == self.name:
                animals["health"] = newhealth
                animals["happiness"] = newhappiness
        print(f"{self.name} has just grabbed a bite to eat (hopefully it wasn't you!). Their energy/health are up by {randhealth}, and their happiness is up by {randhappy}!")

    def play(self):
        randhealth = random.randrange(1, 25)
        randhappy = random.randrange(1, 10)
        self.health -= randhealth
        self.happiness += randhappy
        newhealth = self.health
        newhappiness = self.happiness
        for animals in all_animals:
            if animals["name"] == self.name:
                animals["health"] = newhealth
                animals["happiness"] = newhappiness
        print(f"{self.name} has just played for a bit! Their happieness is up by {randhappy}, but their health and energy are down by {randhealth}.")
    
    def captivity(self):
        randhealth = random.randrange(1, 10)
        randhappy = random.randrange(10, 30)
        animalname = self.name
        self.health -= randhealth
        self.happiness -= randhappy
        newhealth = self.health
        newhappiness = self.happiness
        for animals in all_animals:
            if animals["name"] == animalname:
                animals["health"] = newhealth
                animals["happiness"] = newhappiness
        print(f"{self.name} has just remembered that their in a zoo, locked away. Their health and energy are down by {randhealth}, and their happiness is down by {randhappy}.")

    def sleep(self):
        randhealth = random.randrange(15, 30)
        randhappy = random.randrange(1, 10)
        self.health += randhealth
        self.happiness += randhappy
        newhealth = self.health
        newhappiness = self.happiness
        for animals in all_animals:
            if animals["name"] == self.name:
                animals["health"] = newhealth
                animals["happiness"] = newhappiness
        print(f"{self.name} has just slept! Health/Energy is up by {randhealth} and happiness is up by {randhappy}!!")

class Animal(Zoo):
    def __init__(self, health = 50, happiness = 50):
        self.health = health
        self.happiness = happiness

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.animalclass = 'Lion'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})
        print(f"A lion named {self.name} has just been added to the zoo.")

class Tiger(Animal):
    def __init__(self, name, age, stripes):
        super().__init__()
        self.name = name
        self.age = age
        self.stripes = stripes
        self.animalclass = 'Tiger'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})
        print(f"A tiger named {self.name} has just been added to the zoo.")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.animalclass = 'Bear'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})
        print(f"A bear named {self.name} has just been added to the zoo. Oh my!")

def display_animals():
    print("-" * 60)
    for animal in all_animals:
        print(animal)
    print("-" * 60)

MyZoo = Zoo("Erin's Zoo")

Tony = Tiger("Tony", 3, 50)

Simba = Lion("Simba", 25)

Paddington = Bear("Paddington", 2)

display_animals()

Tony.feed()
Tony.play()
Simba.play()
Paddington.play()

display_animals()

Tony.captivity()
Simba.captivity()
Paddington.captivity()

display_animals()

Simba.feed()
Paddington.feed()
Tony.sleep()

display_animals()

Paddington.sleep()
Simba.sleep()
Tony.play()

display_animals()



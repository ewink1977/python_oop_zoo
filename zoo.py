# Zoo (Optional) Python OOP
# Erin Winking

all_animals = []

class Animal:
    def __init__(self, health = 50, happiness = 50):
        self.health = health
        self.happiness = happiness

    def feed(self):
        self.health += 10
        self.happiness += 5
        newhealth = self.health
        newhappiness = self.happiness
        for animals in all_animals:
            if animals["name"] == self.name:
                animals["health"] = newhealth
                animals["happiness"] = newhappiness

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.animalclass = 'Lion'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})

class Tiger(Animal):
    def __init__(self, name, age, stripes):
        super().__init__()
        self.name = name
        self.age = age
        self.stripes = stripes
        self.animalclass = 'Tiger'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.animalclass = 'Bear'
        all_animals.append({"class" : self.animalclass, "name" : self.name, "age" : self.age, "health" : self.health, "happiness" : self.happiness})

def display_animals():
    print("-" * 60)
    for animal in all_animals:
        print(animal)
    print("-" * 60)

# display_animals()
Tony = Tiger("Tony", 3, 50)

Simba = Lion("Simba", 25)

Paddington = Bear("Paddington", 2)

display_animals()

Tony.feed()

display_animals()
# print(all_animals)

# print(Tony)




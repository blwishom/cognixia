class Dog:
  def __init__(self, name, breed, age = 0, friendliness = True):
    self.name = name
    self.breed = breed
    self.age = age
    self.is_friendly = friendliness

  def __repr__(self):
    description = "This {breed} named {name} is {age} years old. ".format(breed = self.breed, name = self.name, age=self.age)
    if self.is_friendly:
      description += f"{self.name} is a friendly dog."
    else:
      description += "{name} is an unfriendly dog.".format(name = self.name)
    return description

dog1 = Dog("Barker", "Husky", 3)
dog2 = Dog("Rocky", "Cane Corso", 7, False)

print(dog1)
print(dog2)



class Turtle:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def __repr__(self):
        description = f"{self.name} is {self.age} years old and move at a {self.speed} pace."
        return description


Turtle1 = Turtle('Pokey', 86, 'slow')
Turtle2 = Turtle('Speedy', 27, 'medium')

print(Turtle1)
print(Turtle2)

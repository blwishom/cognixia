class Dog:
  def __init__(self, name, breed, age = 0, friendliness = True):
    self.name = name
    self.breed = breed
    self.age = age
    self.is_friendly = friendliness

dog1 = Dog("Barker", "Husky", 3)
dog2 = Dog("Rocky", "Cane Corso", 7, False)

class Dog:
  def __init__(self, name, breed, age = 0, friendliness=True):
    self.name = name
    self.breed = breed
    self.age = age
    self.is_friendly = friendliness
    self.friends = []

  def __repr__(self):
    description = "This {breed} named {name} is {age} years old and has {number_of_friends} friends.".format(breed = self.breed, name = self.name, age=self.age, number_of_friends=len(self.friends))
    if self.is_friendly:
      description += f"{name} is a friendly dog."
    else:
      description += "{name} is an unfriendly dog.".format(name = self.name)
    return description



class Turtle:
  def __init__(self, name, age, speed):
    self.name = name,
    self.age = age,
    self.speed = speed

Turtle1 = Turtle('Pokey', 86, 'slow')
Turtle2 = Turtle('Speedy', 27, 'medium')

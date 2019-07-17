from enum import Enum

class Potato:
    def __init__(self, name, happy=100, health=100, hunger=100):
      self.name = name
      self.happy = happy
      self.health = health
      self.hunger = hunger
      # self.state = StatePotato(state)

class StatePotato (Enum):
  SAD = 0
  NORMAL = 1
  SICK = 2
  TIRED = 3
  DIRTY = 4
  SLEEPING = 5
  DEAD = 6

  def getImage (self):
    print(self.name)
    if self.name == 'SAD':
      print('Yess')

# def test ():
#   state1 = StatePotato.SAD
#   StatePotato.getImage(state1)

# test()
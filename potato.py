from enum import Enum

class Application:
    def __init__(self):
      self.happy = 100
      self.health = 100
      self.hunger = 100
      self.state = StatePotato.NORMAL

class StatePotato (Enum):
  SAD = 0
  NORMAL = 1
  SICK = 2
  TIRED = 3
  DIRTY = 4
  SLEEPING = 5
  DEAD = 6

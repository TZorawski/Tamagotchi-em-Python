from enum import Enum

class Potato:
  # Variáveis estáticas
  minHunger = 50
  maxHunger = 100
  minHealth = 60
  maxHealth = 100
  minHappy = 50
  maxHappy = 100
  minClean = 40
  maxClean = 100
  minEnergy = 50
  maxEnergy = 100
  goodRate = 80
  fineRate = 50

  def __init__(self, name, happy=100, health=100, hunger=100, clean=100, energy=100):
    self.name = name
    self.happy = happy
    self.health = health
    self.hunger = hunger
    self.clean = clean
    self.energy = energy
    self.state = StatePotato.NORMAL

  # def getHunger (self):
  #   return self.hunger
  
  def getRates (self):
    rates = [self.happy, self.health, self.hunger, self.clean, self.energy]
    return rates


  def toEat (self, growVal):
    self.hunger = self.hunger + growVal
    # print("Fome: " + str(self.hunger))
    self.updateState()

  def toCure (self, growVal):
    self.health = self.health + growVal
    self.updateState()
  
  def toSleep (self, growVal):
    if self.energy < self.maxEnergy:
      self.energy = self.energy + growVal
      self.updateState()
    self.state = StatePotato.SLEEPING

  def toWakeUp (self):
    if self.state == StatePotato.SLEEPING:
      self.updateState()

  def toClean (self, growVal):
    if self.clean < self.maxClean:
      self.clean = self.clean + growVal
      self.updateState()

  def getState (self):
    return self.state

  def updateState (self):
    if (self.hunger > self.maxHunger) or (self.health > self.maxHealth):
      # print("entrou")
      self.health = self.minHealth
      self.state = StatePotato.SICK
    
    elif self.health <= self.minHealth:
      self.state = StatePotato.SICK

    elif self.happy <= self.minHappy:
      self.state = StatePotato.SAD

    elif self.energy <= self.minEnergy:
      self.state = StatePotato.TIRED

    elif self.clean <= self.minClean:
      self.state = StatePotato.DIRTY

    elif (self.happy >= self.goodRate) and (self.health >= self.goodRate) and (self.hunger >= self.goodRate)  and (self.energy >= self.fineRate):
      self.state = StatePotato.HAPPY

    elif (self.happy <= 0) or (self.health <= 0) or (self.hunger <= 0) or (self.clean <= 0) or (self.energy <= 0) :
      self.state = StatePotato.DEAD

    else:
      self.state = StatePotato.NORMAL

    return self.state
    

class StatePotato (Enum):
  SAD = 0
  NORMAL = 1
  SICK = 2
  TIRED = 3
  DIRTY = 4
  SLEEPING = 5
  HAPPY = 6
  DEAD = 7

  def getImage (self):
    # print(self.name)
    path_dir = 'images/'
    if self.name == 'SAD':
      return path_dir + 'sad.gif'
    elif self.name == 'NORMAL':
      return path_dir + 'normal.gif'
    elif self.name == 'HAPPY':
      return path_dir + 'happy.gif'
    elif self.name == 'SICK':
      return path_dir + 'sick.gif'
    elif self.name == 'TIRED':
      return path_dir + 'tired.gif'
    elif self.name == 'DIRTY':
      return path_dir + 'dirty.gif'
    elif self.name == 'SLEEPING':
      return path_dir + 'sleeping3.gif'
    elif self.name == 'DEAD':
      return path_dir + 'dead.gif'
    
    

# def test ():
#   state1 = StatePotato.SAD
#   StatePotato.getImage(state1)

# test()
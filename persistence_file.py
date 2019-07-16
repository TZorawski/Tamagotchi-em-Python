import sys

# Recupera todos os dados do usuário
def read_file(file_name):
    config = {}
    transition = {}

    aux = 0
    file = open(file_name, 'r')
    lines = file.readlines()
    pets = []
    
    for l in lines:
        features = l.strip('\n').split(',')
        pets.append(features)
    
    return pets

# Recupera o pet do usuário
def getPet (ownerName, petName):
  features = read_file('data/' + ownerName + '.txt')
  for f in features:
    if f[0] == petName:
      return f
  return []

def teste():
    # pets = read_file("data/marcos.txt")
    # for p in pets:
    #   print(p)

    print(getPet('marcos', 'nome1'))

teste()
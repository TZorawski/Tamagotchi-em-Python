import sys

# Recupera todos os dados do usuário
# Retorna uma lista de listas de string
def read_file (file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    pets = []
    
    for l in lines:
        features = l.strip('\n').split(',')
        pets.append(features)
    
    file.close()

    return pets

# Recupera todos os dados do usuário
# Retorna uma lista com as linhas
def read_file_only_lines (file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    
    file.close()

    return lines

# Recupera o pet do usuário
def getPet (ownerName, petName):
  features = read_file('data/' + ownerName + '.txt')
  for f in features:
    if f[0] == petName:
      return f
  return []

# Recupera a posição do pet no arquivo do usuário
def getPetPos (ownerName, petName):
  features = read_file('data/' + ownerName + '.txt')
  i = 0
  for f in features:
    if f[0] == petName:
      return i
      i = i + 1
  return -1

# Guarda os dados do usuário
def write_file(ownerName, petName, features):
  pos = getPetPos(ownerName, petName)
  path = 'data/' + ownerName + '.txt'
  lines = read_file_only_lines(path)
  file = open(path, 'w')
  print(lines)
  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

  lines[pos] = features + '\n'
  text = ''
  
  for l in lines:
      text = text + l
  # print("????????????????????????????????????????????????????????")
  print(text)
  
  file.write(text)
  file.close()

def teste():
  # ======= Lendo dados =======
  # pets = read_file("data/marcos.txt")
  # for p in pets:
  #   print(p)

  # print(getPet('marcos', 'nome1'))


  # ======= Escrevendo dados =======
  write_file('ana', 'bomerang', 'horacio,150720192356,50,60,45')

teste()
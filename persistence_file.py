import sys

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

def teste():
    pets = read_file("data/marcos.txt")
    
    for p in pets:
      print(p)

teste()
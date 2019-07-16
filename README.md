# Tamagotchi-em-Python
Tamagotchi em Python desenvolvido para a disciplina de Linguagem de Programação do curso de Ciência da Computação da UTFPR de Campo Mourão.

# É um programa de batatas. Olha os gifs de batatinhas :)
Para executar use 'python home_screen.py'.

## Organização
### images/
Guarda todas as imagens do Pet.

### data/
Guarda todos os arquivos com dados dos usuários e seus pets.

O nome do arquivo representa o usuário e dentro dele estão os dados de todos os pets daquele usuário. Cada linha guarda os seguintes atributos, nessa ordem: name, last_visit, rateHappy, rateHealth, rateHungry.

Cada pet é identificado pelo seu nome. Last visit guarda a hora e data da última visita para os cálculos das taxas.
### home_screen.py
Tela inicial do programa. É onde o usuário se identifica e escolhe qual Pet deseja abrir.

### tamagotchi.py
Guarda a GUI do programa ligada ao Pet.

### potato.py
Guarda tudo relacionado ao personagem, como estado, ações, etc. Seus estados são controlados por um 'enum', o qual guarda todas as possibilidades de estado do pet.

## O que falta fazer?
- Persistência (um usuário pode ter mais de um tamagotchi)
- Implementar regra de vida do personagem
- Playgame

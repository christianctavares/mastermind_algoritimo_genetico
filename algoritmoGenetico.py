from random import choices
from typing import List
from operator import itemgetter
import sys
import random

Genome = List[int]
Population = List[Genome]

# VARIABLE DECLARATION #
WEIGHT_BLACK = 5 
WEIGHT_WHITE = 3 
CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY = 0.03
TOGUESS = []

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'

def generate_genome(length: int) -> Genome:
    return choices([1,2,3,4,5,6], k=length)

def generate_population(size: int, genome_lenght: int) -> Population:
    return [generate_genome(genome_lenght) for _ in range(size)]

def fitness(genome: Genome, guess: TOGUESS):
    value = 0 
    for i, j in zip(genome, guess):
        if i == j:
            value += WEIGHT_BLACK
        elif i in guess:
            value += WEIGHT_WHITE
    if value == 0:
        return 0
    return value

def crossover(code1, code2):
    newCode = []
    for i in range(4):
        if random.random() > CROSSOVER_PROBABILITY:
            newCode.append(code1[i])
        else:
            newCode.append(code2[i])
    return newCode

def mutate(code):
    position = random.randint(0, 3)
    newValue = random.randint(1, 6)
    code[position] = newValue
    return code

def new_population(parents):
    sons = []
    for i in range(len(parents)):
        if i == len(parents) - 1:
            sons.append(parents[i])
            break
        son = crossover(parents[i], parents[i+1])
        if random.random() <= MUTATION_PROBABILITY:
            son = mutate(son)     
        sons.append(son)
    return sons

def ranked_func(solutions):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append([fitness(s, TOGUESS), s])
    rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)
    return rankedsolutions

def cross_mutate(bestsolutions):
    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
        elements.append(s[1][3])
    new_gen = []
    for j in range(60):
        e_1 = random.choice(elements)
        e_2 = random.choice(elements)
        e_3 = random.choice(elements)
        e_4 = random.choice(elements)
        new_gen.append([e_1,e_2,e_3,e_4])
    #print("New Gen 1", new_gen)
    if random.random() <= MUTATION_PROBABILITY:
        m = random.random
        new_gen[m] = mutate(new_gen[m])
        #print("New Gen 2", new_gen)
    return new_gen

def ai():
    popu = generate_population(60, 4)
    solutions = []
    for s in popu:
        solutions.append(s)
    count = 0
    for i in popu:
        count += 1
        rankedsolutions = ranked_func(solutions)
        bestsolutions = rankedsolutions[:19]
        solutions = cross_mutate(bestsolutions)
        rankedsolutions = ranked_func(solutions)
        count += 1
        if rankedsolutions[0][0] >=16:
            return rankedsolutions[0][1] 

def game(attempt):
    chances = 8
    move = 1
    if attempt == TOGUESS:
        print()
        print(f"{move}° Jogada realizada: {attempt}")
        print()
        print(bcolors.OKGREEN + "█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
        print(bcolors.OKGREEN + "▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
        print()
        print("==== Você acertou de PRIMEIRA! Parabens ====")
        print()
    else:
        round = 0
        while attempt != TOGUESS or chances == 0:
            if chances == 0:
                print()
                print(bcolors.FAIL + "█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█")
                print(bcolors.FAIL + "█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄")
                print()
                print("Acabou suas chances de acertar (╯°□°）╯︵ ┻━┻")            
                return
            round += 1
            count =  0

            hits = ['X','X','X','X']

            for i in range(0, 4):
                if(attempt[i] == TOGUESS[i]):
                    count += 1
                    hits[i] = attempt[i]
                else:
                    continue

            if count < 4 and count != 0:  
                print(f"{move}° Jogada realizada: {attempt}")
                print("Você não achou a sequência, mas encontrou", count, "digito(s) corretos")
                print("Números corretos:")
                for k in hits:
                    print(k, end=' ')
                print('\n')
                chances -= 1
                move += 1
                attempt = ai()
            elif count == 0:
                print(f"{move}° Jogada realizada: {attempt}")
                print("Nenhum dos números escolhidos eram corretos")
                print('\n')
                chances -= 1
                move += 1
                attempt = ai()

        if attempt == TOGUESS:  
            round += 1
            chances -= 1
            print(f"{move}° Jogada realizada: {attempt}")
            print("Você achou a sequência de digitos corretos!")
            print()
            print(bcolors.OKGREEN + "█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
            print(bcolors.OKGREEN + "▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
            print()
            print("==== Você acertou em",round,"tentativas ====")
            print()

# MAIN #
senha = []

for i in range(1, 5):
    valor = input(f'\nInsira o {i}º valor da senha: ')
    while (valor.isnumeric() != True or int(valor) < 0 or int(valor) > 6):
        print("O valor inserido deve ser númerico e entre 0 e 6\n")
        valor = input(f'\nInsira novamente o {i}º valor da senha: ')
    senha.append(int(valor))
TOGUESS = senha
print(f"\nSENHA escolhida: {TOGUESS}\n")
game(ai())
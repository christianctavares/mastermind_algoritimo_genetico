from random import choices
from typing import List
from operator import itemgetter
import random

Genome = List[int]
Population = List[Genome]

# VARIABLE DECLARATION #
WEIGHT_BLACK = 5 
WEIGHT_WHITE = 3 
CROSSOVER_PROBABILITY = 0.5
MUTATION_PROBABILITY = 0.03
TOGUESS = []

SELECTED_SOLUTIONS = 20
PONTUACAO_FITNESS_ACEITAVEL = 16
NUMERO_DA_POPULACAO = 60
TAMANHO_DO_GENOMA = 4

class ConsoleCores:
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

def ranked_func(solutions):
    rankedsolutions = []
    for solution in solutions:
        rankedsolutions.append([fitness(solution, TOGUESS), solution])
    rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)
    return rankedsolutions

def cross_mutate(best_solutions):
    elements = []
    for solution in best_solutions:
        elements.append(solution[1][0])
        elements.append(solution[1][1])
        elements.append(solution[1][2])
        elements.append(solution[1][3])
    new_gen = []
    for j in range(NUMERO_DA_POPULACAO):
        e_1 = random.choice(elements)
        e_2 = random.choice(elements)
        e_3 = random.choice(elements)
        e_4 = random.choice(elements)
        new_gen.append([e_1,e_2,e_3,e_4])

    return new_gen

def ai():
    popu = generate_population(NUMERO_DA_POPULACAO, TAMANHO_DO_GENOMA)
    solutions = popu

    for i in popu:
        rankedsolutions = ranked_func(solutions)
        best_solutions = rankedsolutions[:SELECTED_SOLUTIONS]
        solutions = cross_mutate(best_solutions)
        rankedsolutions = ranked_func(solutions)
        if rankedsolutions[0][0] >= PONTUACAO_FITNESS_ACEITAVEL:
            return rankedsolutions[0][1]

def game(attempt):
    chances = 8
    move = 1
    if attempt == TOGUESS:
        print()
        print(f"{move}° Jogada realizada: {attempt}")
        print()
        print(ConsoleCores.OKGREEN + "█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
        print(ConsoleCores.OKGREEN + "▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
        print()
        print("==== Você acertou de PRIMEIRA! Parabens ====")
        print()
    else:
        round = 0
        while attempt != TOGUESS or chances == 0:
            if chances == 0:
                print()
                print(ConsoleCores.FAIL + "█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█")
                print(ConsoleCores.FAIL + "█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄")
                print()
                print("Acabou suas chances de acertar (╯°□°）╯︵ ┻━┻")            
                return
            round += 1
            count =  0

            hits = ['X','X','X','X']

            for peca in range(0, 4):
                if(attempt[peca] == TOGUESS[peca]):
                    count += 1
                    hits[peca] = attempt[peca]
                else:
                    continue

            if count < 4 and count != 0:  
                print(f"{move}° Jogada realizada: {attempt}")
                print("Você não achou a sequência, mas encontrou", count, "digito(s) corretos")
                print("Números corretos:")
                for numeros in hits:
                    print(numeros, end=' ')
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
            print(ConsoleCores.OKGREEN + "█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
            print(ConsoleCores.OKGREEN + "▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
            print()
            print("==== Você acertou em",round,"tentativas ====")
            print()

# MAIN #
senha = []

for posicao in range(1, 5):
    valor = input(f'\nInsira o {posicao}º valor da senha: ')
    while (valor.isnumeric() is not True or int(valor) < 0 or int(valor) > 6):
        print("O valor inserido deve ser númerico e entre 0 e 6\n")
        valor = input(f'\nInsira novamente o {posicao}º valor da senha: ')
    senha.append(int(valor))
TOGUESS = senha
print(f"\nSENHA escolhida: {TOGUESS}\n")
game(ai())

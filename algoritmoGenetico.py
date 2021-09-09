from random import choices
from typing import List
from operator import itemgetter
import random 

TOGUESS = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
print()
print("SENHA GERADA: ", TOGUESS)

Genome = List[int]
Population = List[Genome]
WEIGHT_BLACK = 5 
WEIGHT_WHITE = 3 

def robo():
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

    def cross_mutate(bestsolutions):
        elements = []
        for s in bestsolutions:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
            elements.append(s[1][3])
        new_gen = []
        #mudar popu
        for j in range(60):
            e_1 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e_2 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e_3 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e_4 = random.choice(elements) #* random.uniform(0.99, 1.01)

            new_gen.append([e_1,e_2,e_3,e_4])
        return new_gen
    
    popu = generate_population(60, 4)
    solutions = []
    for s in popu:
        solutions.append(s)

    for i in popu:
        rankedsolutions = []
        for s in solutions:
            rankedsolutions.append([fitness(s, TOGUESS), s])
        rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)
        #print(f"--- Genoma {i[0]} best solution === ")
        #print(rankedsolutions[0])

        if rankedsolutions[0][0] >16:
            tentativa = rankedsolutions[0][1]
            # print("TENTATIVA: ", tentativa)
            # print("SENHA CORRETA: ",TOGUESS)
            return tentativa

        #mudar popu
        bestsolutions = rankedsolutions[:19]
        solutions = cross_mutate(bestsolutions)

        for s in solutions:
            rankedsolutions.append([fitness(s, TOGUESS), s])
        rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)

def game(tentativa):
    chances = 8
    jogada = 1
    if tentativa == TOGUESS:
        print()
        print(f"{jogada}° Jogada realizada: {tentativa}")
        print()
        print("█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
        print("▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
        print()
        print("==== Você acertou de PRIMEIRA! Parabens ====")
        print()
    else:
        rodada = 0

        while tentativa != TOGUESS:
            if chances == 0:
                print()
                print("█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█")
                print("█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄")
                print()
                print("Acabou suas chances de acertar =(")            
                return
            rodada += 1
            count =  0

            acertos = ['X','X','X','X']

            for i in range(0, 4):
                
                if(tentativa[i] == TOGUESS[i]):
                    count += 1
                    acertos[i] = tentativa[i]
                else:
                    continue
            
            if count < 4 and count != 0:  
                print(f"{jogada}° Jogada realizada: {tentativa}")
                print("Você não achou a sequência, mas encontrou", count, "digito(s) corretos")
                print("Números corretos:")
                for k in acertos:
                    print(k, end=' ')
                print('\n')
                chances -= 1
                jogada += 1
                tentativa = robo()
            elif count == 0:
                print(f"{jogada}° Jogada realizada: {tentativa}")
                print("Nenhum dos números escolhidos eram corretos")
                chances -= 1
                jogada += 1
                tentativa = robo()

        if tentativa == TOGUESS:  
            rodada += 1
            chances -= 1
            print(f"{jogada}° Jogada realizada: {tentativa}")
            print("Você achou a sequência de digitos corretos!")
            print()
            print("█░█ █ ▀█▀ █▀█ █▀█ █ ▄▀█ █")
            print("▀▄▀ █ ░█░ █▄█ █▀▄ █ █▀█ ▄")
            print()
            print("==== Você acertou em",rodada,"tentativa ====")
            print()

def jogar():
    tentativa = robo()
    game(tentativa)

jogar()
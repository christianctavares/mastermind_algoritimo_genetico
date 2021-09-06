import random

from random import choices
from typing import List
from collections import namedtuple
from operator import itemgetter
import random 

senha = [random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]
print(senha)

TOGUESS = senha

Genome = List[int]
Population = List[Genome]
WEIGHT_BLACK = 5 
WEIGHT_WHITE = 3 

global tentativa
tentativa = []
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
                    # print ('{0} e {1} sao o msm valor e msm posicao'.format(i, j))
                elif i in guess:
                    value += WEIGHT_WHITE
                    # print ('{0} tem o valor correto mas esta na posicao errada'.format(i))
        if value == 0:
            return 0
        return value
    #mudar popu
    popu = generate_population(60, 4)
    solutions = []
    for s in popu:
        solutions.append(s)
        
    #print(solutions)

    for i in popu:
        rankedsolutions = []
        for s in solutions:
            #rankedsolutions.append((fitness(s, TOGUESS)))
            rankedsolutions.append([fitness(s, TOGUESS), s])
    #rint(rankedsolutions)
        rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)

        #print(rankedsolutions[0])
        if rankedsolutions[0][0] >16:
            tentativa = rankedsolutions[0][1]
            print("TENTATIVA: ", tentativa)
            print("SENHA: ",senha)
            return tentativa
            break

        #print(f"--- Get {rankedsolutions[0][0]} best solution --- ")
        #mudar popu
        bestsolutions = rankedsolutions[:19]
        #print(bestsolutions)
        elements = []
        for s in bestsolutions:
            elements.append(s[1][0])
            elements.append(s[1][1])
            elements.append(s[1][2])
            elements.append(s[1][3])
        newGen = []
        #mudar popu
        for _ in range(60):
            e1 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e2 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e3 = random.choice(elements) #* random.uniform(0.99, 1.01)
            e4 = random.choice(elements) #* random.uniform(0.99, 1.01)

            newGen.append([e1,e2,e3,e4])
        solutions = newGen
        for s in solutions:
            rankedsolutions.append([fitness(s, TOGUESS), s])
        rankedsolutions = sorted(rankedsolutions, key=itemgetter(0), reverse=True)

tentativa = robo()
if(tentativa == senha):
    print("==== Você acertou em 1 tentativa ====")
else:
    rodada = 0
    
    while(tentativa != senha):
        rodada += 1
        count =  0


        acertos = ['X','X','X','X']

        for i in range(0, 4):
            # print("Tentativa:",tentativa)
            # print("Senha",senha)
            if(tentativa[i] == senha[i]):
                count += 1
                acertos[i] = tentativa[i]
            else:
                continue
        
        if (count < 4) and (count != 0):  
            print("Você não achou a sequência, mas encontrou", count, "digito(s) corretos")
            print("Números corretos:")
            for k in acertos:
                print(k, end=' ')
            print('\n')
            tentativa = robo()
        elif (count == 0):  
            print("Nenhum dos números escolhidos eram corretos")
            tentativa = robo()

    if tentativa == senha:  
        print("==== Você acertou em", rodada,"tentativa ====")